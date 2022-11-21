#!/usr/bin/env python3
# coding:utf-8

# default libraries
# install libraries
import pandas as pd
import tables
from tqdm import tqdm

#local libraries
from script.python import Pangenome


res_col_names = ['Gene_family', 'Annotation', 'Accession', 'e_value', 'score', 'overlap', 'Description']


def card_parse(file: str):
    column = {"ARO": "Accession", "Contig": "Gene_family", "Best_Hit_Bitscore": "score",
              "Best_Hit_ARO": "protein_name", "ID": "secondary_name"}
    card_df = pd.read_csv(file, sep="\t", header=0, index_col=None,
                          usecols=["ARO", "Contig", "Best_Hit_ARO", "ID", "Best_Hit_Bitscore",
                                   "Drug Class", "Resistance Mechanism", "AMR Gene Family"])
    concat_cols = card_df["Drug Class"] + ", " + card_df["Resistance Mechanism"] + ", " + card_df["AMR Gene Family"]

    card_df = card_df.drop(columns=["Drug Class", "Resistance Mechanism", "AMR Gene Family"])
    card_df.insert(card_df.shape[1], "Description", concat_cols, True)
    card_df.rename(columns=column, inplace=True)
    card_df["Gene_family"] = card_df["Gene_family"].str.replace('_[0-9]\s?$', '', regex=True)
    return card_df[['Gene_family', 'Accession', 'protein_name', 'score', 'secondary_name', 'Description']]


def annotation_to_families(annotation_df: pd.DataFrame, pangenome: Pangenome, source: str = None) -> dict:
    """ Add to gene families an annotation and create a dictionary with for each annotation a set of gene family

    :param annotation_df: Dataframe with for each family an annotation
    :param pangenome: Pangenome with gene families
    :param source: source of the annotation

    :return: Dictionary with for each annotation a set of gene family
    """
    for gf in annotation_df[res_col_names[0]].unique():
        select_df = annotation_df.loc[annotation_df[res_col_names[0]] == gf]
        gene_fam = pangenome.get_gene_family(name=gf)
        if gene_fam is not None:
            gene_fam.add_annotation(source=source, annotation=list(select_df['protein_name']))


def gene_annot_desc(max_annotation_len: int = 1, max_fam_len: int = 1) -> dict:
    """
    Create a formated table for gene families description
    :param max_annotation_len: Maximum size of gene family name
    :param max_fam_len: Maximum size of gene family representing gene sequences
    :return: Formated table
    """
    return {
        "annotation": tables.StringCol(itemsize=max_annotation_len),
        "geneFam": tables.StringCol(itemsize=max_fam_len)
    }


def get_annot_len(pangenome: Pangenome, source: str) -> (int, int):
    """
    Get maximum size of gene families information
    :param pangenome: Pangenome with gene families computed
    :param source: Name of the annotation source
    :return: Maximum size of each element
    """
    max_annotation_len = 1
    max_fam_len = 1
    expected_rows = 0

    for genefam in pangenome.get_gf_by_annnotation(source=source):
        if len(genefam.name) > max_fam_len:
            max_fam_len = len(genefam.name)
        for annot in genefam.annotation[source]:
            if len(annot) > max_annotation_len:
                max_annotation_len = len(annot)
            expected_rows += 1

    return max_annotation_len, max_fam_len, expected_rows


def write_gene_fam_annot(pangenome: Pangenome, h5f: tables.File, force: bool = False, disable_bar: bool = False):
    """
    Writing a table containing the protein sequences of each family
    :param pangenome: Pangenome with gene families computed
    :param h5f: HDF5 file to write gene families
    :param force: force to write information if precedent information exist
    :param disable_bar: Disable progress bar
    """
    if '/geneFamiliesAnnot' in h5f and force is True:
        print("Erasing the formerly computed gene family annotations...")
        h5f.remove_node('/', 'geneFamiliesAnnot', recursive=True)  # erasing the table, and rewriting a new one.
    annot_group = h5f.create_group("/", "geneFamiliesAnnot", "Gene families functional annotation")
    for source in pangenome.annotation_source:
        max_annotation_len, max_fam_len, expected_rows = get_annot_len(pangenome, source)
        source_table = h5f.create_table(annot_group, source, gene_annot_desc(max_annotation_len, max_fam_len),
                                        expectedrows=expected_rows)
        annot_row = source_table.row
        for genefam in tqdm(pangenome.get_gf_by_annnotation(source=source),
                            unit="annot", disable=disable_bar):
            for annot in genefam.annotation[source]:
                annot_row["annotation"] = annot
                annot_row["geneFam"] = genefam.name
                annot_row.append()
        source_table.flush()

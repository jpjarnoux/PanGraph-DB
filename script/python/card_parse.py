#!/usr/bin/env python3
# coding:utf-8

# default libraries
# install libraries
import pandas as pd


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


if __name__ == "__main__":
    file = "/home/jarnoux/Projects/PANORAMA/testingDataset/db/GF_fasta/ESKAPE/card_res/card_res.txt"
    out = "/home/jarnoux/Projects/PANORAMA/testingDataset/db/GF_fasta/ESKAPE/card_res/card_res.tsv"

    df = card_parse(file)
    df.to_csv(out, sep="\t", index=False)

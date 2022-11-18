#!/usr/bin/env python3
# coding:utf-8

# default libraries
from tqdm import tqdm
import uuid

# local libraries
from script.python import Pangenome


def give_gene_tmp_id(pangenome: Pangenome, disable_bar: bool = True):
    for gene in tqdm(pangenome.genes, total=pangenome.number_of_gene(), unit='gene', disable=disable_bar):
        gene.tmp_id = str(uuid.uuid4())


def invert_edges_query(edge_label: str):
    return f"""
        MATCH (f)-[r:{edge_label}]->(s)
        CALL apoc.refactor.invert(r)
        yield input, output
        RETURN input, output"""
#!/usr/bin/env python3
# coding:utf-8

# default libraries
from typing import Union

# installed librairies
from ppanggolin.genome import Organism, Contig
from ppanggolin.edge import Edge
from ppanggolin.region import Module, Region, Spot

# local librairies
from script.python import Pangenome
from script.python import GeneFamily

fam_visit = set()


def get_genes(parent: Union[GeneFamily, Region, Contig]):
    genes_list = []
    for gene in parent.genes:
        genes_list.append({"name": gene.name,
                           "genomic_type": gene.type,
                           "is_fragment": bool(gene.is_fragment),
                           # Prevent TypeError: Object of type bool_ is not JSON serializable
                           "start": gene.start,
                           "stop": gene.stop,
                           "strand": gene.strand,
                           "product": gene.product,
                           "local_id": gene.local_identifier,
                           "tmp_id": gene.tmp_id})
    return genes_list


def write_contig(organism: Organism):
    contig_list = []
    for contig in organism.contigs:
        contig_list.append({"name": contig.name,
                            "is_circular": bool(contig.is_circular),
                            "Gene": get_genes(contig)})
    return contig_list


def write_families(pangenome: Pangenome, out_dict: dict):
    family: GeneFamily
    for family in pangenome.gene_families:
        annot = family.get_annot("CARD")
        fam_dic_property = {"name": family.name,
                            "Partition": {"partition": family.named_partition,
                                          "subpartition": family.partition},
                            "annotation": annot[0] if annot is not None else None,
                            "Gene": get_genes(family),
                            "Family": get_neighbor(family)  # Return neighbor with edges weight
                            }
        # fam_dic_property.update(get_neighbor(family))
        # if family.named_partition == "persistent":
        #     out_dict["Pangenome"]["Family"]["Persistent"].append(fam_dic_property)
        # elif family.named_partition == "shell":
        #     out_dict["Pangenome"]["Family"]["Shell"].append(fam_dic_property)
        # elif family.named_partition == "cloud":
        #     out_dict["Pangenome"]["Family"]["Cloud"].append(fam_dic_property)
        # else:
        #     raise Exception("Unrecognized partition name")
        out_dict["Pangenome"]["Family"].append(fam_dic_property)


def get_neighbor(family: GeneFamily):
    global fam_visit
    edge: Edge
    neighbors = []
    for edge in family.edges:
        if edge.source.name == family.name:
            if edge.target.name not in fam_visit:
                annot = edge.target.get_annot("CARD")
                neighbors.append({"weight": len(edge.organisms),
                                  "name": edge.target.name,
                                  "Partition": {"partition": edge.target.named_partition,
                                                "subpartition": edge.target.partition},
                                  "annotation": annot[0] if annot is not None else None})
        elif edge.target.name == family.name:
            if edge.source.name not in fam_visit:
                annot = edge.source.get_annot("CARD")
                neighbors.append({"weight": len(edge.organisms),
                                  "name": edge.source.name,
                                  "Partition": {"partition": edge.source.named_partition,
                                                "subpartition": edge.source.partition},
                                  "annotation": annot[0] if annot is not None else None})
        else:
            raise Exception("Source and target name are different from edge's family. "
                            "Please check you import graph data and if the problem persist, post an issue.")
    fam_visit.add(family.name)

    return neighbors


def write_organisms(pangenome: Pangenome, out_dict: dict):
    for org in pangenome.organisms:
        out_dict["Pangenome"]["Genome"].append({"name": str(org.name),
                                                "Contig": write_contig(org)})


def write_rgp(parent: Union[Pangenome, Spot]):
    rgp_list = []
    for rgp in parent.regions:
        rgp_list.append({"name": str(rgp.name),
                         "start": rgp.start,
                         "stop": rgp.stop,
                         "score": float(rgp.score),
                         "is_whole_contig": rgp.is_whole_contig,
                         "is_contig_border": rgp.is_contig_border,
                         "Gene": get_genes(rgp)})
    return rgp_list


def write_spot(pangenome: Pangenome, out_dict: dict):
    for spot in pangenome.spots:
        out_dict["Pangenome"]["Spot"].append({"name": f"{str(spot.ID)}",
                                              "RGP": write_rgp(parent=spot)})


def write_modules(pangenome: Pangenome, out_dict: dict):
    module: Module
    for module in pangenome.modules:
        module_dict = {"name": int(module.ID),  # int prevent TypeError: Object of type uint32 is not JSON serializable
                       "Family": []}
        for family in module.families:
            annot = family.get_annot("CARD")
            module_dict["Family"].append({"name": family.name,
                                          "Partition": {"partition": family.named_partition,
                                                        "subpartition": family.partition},
                                          "annotation": annot[0] if annot is not None else None})
        out_dict["Pangenome"]["Module"].append(module_dict)
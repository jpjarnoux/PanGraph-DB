# PanGraph-DB : A Graph Database Framework for Complex Multi-Pangenome Analyses

## About the project

PanGraph-DB is a pipeline capable of operating on a unified graph dataset consisting of multiple pangenome graphs, as computed by the [PPanGGOLiN framework](https://github.com/labgem/PPanGGOLiN), and that further leverages the [Neo4j graph database](https://neo4j.com/) to perform complex analyses. These are expressed at graph queries in Neo4j's [Cypher query language](https://neo4j.com/developer/cypher/).

This repository includes a Jupyter notebook describing performance and scalability experiments performed on datasets of up to 10 pangenomes, with sizes ranging from 200 - 1800 MB, on a workload comprised of 10 queries ([available here](./scipt/python/wf.py)).

| Pangenomes                         | \# of genes | \# of genomes | \# of families | \# raw edges | \# of RGPs | \# of spots | \# of modules | HDF5 size (MB) |
|------------------------------------|-------------|---------------|----------------|--------------|------------|-------------|---------------|----------------|
|*Acinetobacter baumannii*     | 1 044 515   | 285           | 14 400         | 30 147       | 9 764      | 364         | 609           | 616            |
|*Enterobacter bugandensis*  | 526 062     | 118           | 18 143         | 23 734       | 3 424      | 326         | 250           | 212            |
|*Enterobacter cloacae*      | 651 827     | 137           | 22 953         | 32 270       | 6 083      | 292         | 526           | 358            |
|*Enterobacter hormaechei*   | 739 490     | 159           | 18 166         | 29 798       | 5744       | 280         | 742           | 415            |
|*Enterobacter kobei*        | 705 811     | 150           | 20 836         | 29 311       | 5 740      | 181         | 535           | 386            |
|*Enterobacter roggenkampii* | 978 031     | 210           | 26 080         | 40 459       | 8 807      | 319         | 712           | 537            |
|*Enterococcus faecium*      | 570 257     | 207           | 7 889          | 18 627       | 6 195      | 189         | 318           | 301            |
|*Klebsiella pneumoniae*     | 3 100 409   | 600           | 29 139         | 61 865       | 25 014     | 529         | 1 167         | 1 800          |
|*Pseudomonas aeruginosa*    | 1 892 646   | 313           | 23 699         | 42 084       | 10 706     | 543         | 909           | 1200           |
|*Staphylococcus aureus*     | 1 686 977   | 638           | 7 017          | 18 047       | 11 869     | 268         | 203           | 991            |


## Authors
- Jérôme Arnoux, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University
- Angela Bonifati, Liris CNRS, Lyon 1 University
- Alexandra Calteau, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University 
- Stefania Dumbrava, SAMOVAR/Inst. Polytechnique de Paris, ENSIIE 
- Guillaume Gautreau, MetaGenoPolis, Université Paris-Saclay, INRAE, MGP

## Dependencies
We list all required dependencies below. For installation purposes, please follow the instruction in the next section 'Environment configuration'.

Use pip to install:
- dict2graph==2.0.0
- graphio==0.4.0

Use conda to install:
- ppanggolin==1.2.74
- pyhmmer==0.6.3
- py2neo==2021.2.3
- rgi==6.0.1
- genome_updater==0.5.1

Neo4j:
- Add local DBMS with a Neo4j version of 4.4.11
- APOC 4.4.0.10 or more
- Optional : Neo4J Desktop 1.5.0

# Dataset

The original dataset is available [here](https://drive.google.com/drive/folders/1eZ7GQgU5tAgfryK31EPV6OP2wVRrj79B?usp=share_link).

# Running the project
To begin, note that you must have an empty Neo4J DMBS (version 4.4.11) open and available with the APOC plugin install (version 4.4.0.10).

To execute the following script, you will need to install some packages. They're listed in the following conda environment file. The *in development* version of PPanGGOLiN is required to satisfy some feature and pangenomes compatibility.

To install the conda environment in the jupyter kernel, please copy and paste the following code in your terminal:
```
git clone https://github.com/labgem/PanGraph-DB.git
conda update -n base -c defaults conda -y
conda env create --file conda-env.yml
conda init bash
conda activate pangraph
git clone -b release1.3 https://github.com/labgem/PPanGGOLiN.git
pip install PPanGGOLiN/.
pip install --user ipykernel
python -m ipykernel install --user --name=pangraph
jupyter notebook --notebook-dir=./PanGraph-DB
```

Next run all the cells to obtain the corresponding results.

# PanGraph-DB : A Graph Database Framework for Complex Multi-Pangenome Analyses

## About the project

PanGraph-DB is a data-centric pipeline capable of operating on a unified graph dataset consisting of multiple pangenome graphs, as computed by the [PPanGGOLiN framework](https://github.com/labgem/PPanGGOLiN), and that further leverages the [Neo4j graph database](https://neo4j.com/) to perform complex analyses. These are expressed as graph database queries in Neo4j's [Cypher query language](https://neo4j.com/developer/cypher/). Note that the methodology is, however, system-agnostic and can be reproduced using any other graph database system.

This repository includes a Jupyter notebook describing performance and scalability experiments performed on datasets of up to 10 pangenomes, with sizes ranging from 200 to 1800 MB, on a workload comprised of 10 queries ([available here](./script/python/wf.py)).

| Pangenomes                                                                                                           | \# of genes | \# of genomes | \# of families | \# raw edges | \# of RGPs | \# of spots | \# of modules | HDF5 size (MB) |
|----------------------------------------------------------------------------------------------------------------------|-------------|---------------|----------------|--------------|------------|-------------|---------------|----------------|
| [*Acinetobacter baumannii*](https://drive.google.com/file/d/1vMw6qKszr3GZjeJibdGRNJOY04xwA5OU/view?usp=share_link)   | 1 044 515   | 285           | 14 400         | 30 147       | 9 764      | 364         | 609           | 616            |
| [*Enterobacter bugandensis*](https://drive.google.com/file/d/1HoXGoRCxEWAbLMd7xt18ZjeAfUeOfqwq/view?usp=share_link)  | 526 062     | 118           | 18 143         | 23 734       | 3 424      | 326         | 250           | 212            |
| [*Enterobacter cloacae*](https://drive.google.com/file/d/1QOEUpcne4vqMgkpwSW3pADf7yRNaCdaB/view?usp=share_link)      | 651 827     | 137           | 22 953         | 32 270       | 6 083      | 292         | 526           | 358            |
| [*Enterobacter hormaechei*](https://drive.google.com/file/d/1R2l7gnZDvTjwL4WrWp6yO3jNs_2I_LEv/view?usp=share_link)   | 739 490     | 159           | 18 166         | 29 798       | 5744       | 280         | 742           | 415            |
| [*Enterobacter kobei*](https://drive.google.com/file/d/1JL0FrAi1Wf-9JCGIJmW2OghzAbl3ZLkS/view?usp=share_link)        | 705 811     | 150           | 20 836         | 29 311       | 5 740      | 181         | 535           | 386            |
| [*Enterobacter roggenkampii*](https://drive.google.com/file/d/1iQuG4WYB5k8UESUCA1LyQqyLvQD1JbDq/view?usp=share_link) | 978 031     | 210           | 26 080         | 40 459       | 8 807      | 319         | 712           | 537            |
| [*Enterococcus faecium*](https://drive.google.com/file/d/1VNLFW0qSNbbwJ4ccNd-R2UFTijMkM3eP/view?usp=share_link)      | 570 257     | 207           | 7 889          | 18 627       | 6 195      | 189         | 318           | 301            |
| [*Klebsiella pneumoniae*](https://drive.google.com/file/d/1hbKz4MSZgJM6ibcsWRFyj4LxPt8-T6nW/view?usp=share_link)     | 3 100 409   | 600           | 29 139         | 61 865       | 25 014     | 529         | 1 167         | 1 800          |
| [*Pseudomonas aeruginosa*](https://drive.google.com/file/d/1SsBbCb765MOrGjBcR0yNuK8dio4xKwnX/view?usp=share_link)    | 1 892 646   | 313           | 23 699         | 42 084       | 10 706     | 543         | 909           | 1200           |
| [*Staphylococcus aureus*](https://drive.google.com/file/d/1ZlJOJ2COVPgAZokB9W4r3rku5bSKEdQS/view?usp=sharing)        | 1 686 977   | 638           | 7 017          | 18 047       | 11 869     | 268         | 203           | 991            |


## Authors
- Jérôme Arnoux, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University
- Angela Bonifati, Liris CNRS, Lyon 1 University
- Alexandra Calteau, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University 
- Stefania Dumbrava, SAMOVAR/Inst. Polytechnique de Paris, ENSIIE 
- Guillaume Gautreau, MetaGenoPolis, Université Paris-Saclay, INRAE, MGP

## Dependencies
We list all required dependencies below. 

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

To execute the `PangenomeGraph.ipynb` script, you will need to first install some packages. 

These are listed in the following conda environment file `conda-env.yml`. 

The *in development* version of PPanGGOLiN is required to satisfy some feature and pangenome compatibility.

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

Next run all the cells to obtain the corresponding results. Don't forget to change the data path.


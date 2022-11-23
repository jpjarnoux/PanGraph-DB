# PanGraph-DB : A Graph Database Framework for Complex Multi-Pangenome Analyses

## About the project

PanGraph-DB is a pipeline capable of operating on a unified graph dataset consisting of multiple pangenome graphs, as computed by the PPanGGOLiN framework, and that further leverages the Neo4j graph database to perform complex analyses. These are expressed at graph queries in Neo4j's Cypher language.

This repository includes a Jupyter notebook describing performance and scalability experiments performed on datasets of up to 10 pangenomes, with sizes ranging from 200 - 1800 MB, on a workload comprised of 10 queries.

## Authors
- Jérôme Arnoux, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University
- Angela Bonifati, Liris CNRS, Lyon 1 University
- Alexandra Calteau, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University 
- Stefania Dumbrava, SAMOVAR/Inst. Poltech de Paris, ENSIIE 
- Guillaume Gautreau, MetaGenoPolis, Universit ́e Paris-Saclay, INRAE, MGP

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

Neo4J:
- Add local DBMS with a Neo4j version of 4.4.11
- APOC 4.4.0.10 or more
- Optional : Neo4J Desktop 1.5.0

# Running the project
To begin, note that you must have an empty Neo4J DMBS (version 4.4.11) open and available with the APOC plugin install (version 4.4.0.10).

To execute the following script, you will need to install some packages. They're listed in the following conda environment file. The *in development* version of PPanGGOLiN is required to satisfy some feature and pangenomes compatibility.

To install the conda environment in jupyter kernel, please copy and paste the following code in your terminal:
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
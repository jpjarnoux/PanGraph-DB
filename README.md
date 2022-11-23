# PanGraph-DB : A Graph Database Framework for Complex Multi-Pangenome Analyses

## About the project

PanGraph-DB is a pipeline capable of operating on a unified graph dataset consisting of multiple pangenome graphs, as computed by the PPanGGOLiN framework, and that further leverages the Neo4j graph database to perform complex analyses. These are expressed at graph queries in Neo4j's Cypher language.

The repository includes a Jupyter notebook describing performance and scalability experiments performed on datasets of up to 10 pangenomes, with sizes ranging from 200 - 1800 MB, on a workload comprised of 10 queries.

## Authors
- Jérôme Arnoux, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University
- Angela Bonifati, Liris CNRS, Lyon 1 University
- Alexandra Calteau, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University 
- Stefania Dumbrava, SAMOVAR/Inst. Poltech de Paris, ENSIIE 
- Guillaume Gautreau, MetaGenoPolis, Universit ́e Paris-Saclay, INRAE, MGP

## Dependencies
Below is listed all dependencies. To install it, you can follow the step in the next section 'Environment configuration'. If you prefer you can construct your own environment by installing the dependencies listed below.

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

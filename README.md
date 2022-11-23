# PanGraph-DB : A Graph Database Framework for Complex Multi-Pangenome Analyses

## About the project

PanGraph-DB is a pipeline capable of operating on a unified graph dataset consisting of multiple pangenome graphs, as computed by the [PPanGGOLiN framework] (https://github.com/labgem/PPanGGOLiN), and that further leverages the [Neo4j graph database] (https://neo4j.com/) to perform complex analyses. These are expressed at graph queries in Neo4j's [Cypher query language] (https://neo4j.com/developer/cypher/).

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

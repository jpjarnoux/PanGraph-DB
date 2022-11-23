# PanGraph-DB
A jupyter notebook to reproduce the results of a paper co-authored by the people listed below and under submission to the ICDE conference.

# Authors
- Jérôme Arnoux, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University
- Angela Bonifati, Liris CNRS, Lyon 1 University
- Alexandra Calteau, Genoscope/LABGeM - CEA, CNRS, Paris Saclay University 
- Stefania Dumbrava, SAMOVAR/Inst. Poltech de Paris, ENSIIE 
- Guillaume Gautreau, MetaGenoPolis, Universit ́e Paris-Saclay, INRAE, MGP

# Dependencies
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

# Reference
1. S. Sakr _qnd al_. “The future is big graphs: a community view on graph processing systems,” Commun. ACM, vol. 64, no.9, pp. 62–71, 2021.
2. G. Gautreau _and al_. “PPanGGOLiN: Depicting microbial diversity via a partitioned pangenome graph,” vol. 16, no. 3, p. e1007732, publisher: Public Library of Science. [https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007732](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007732)
3. 
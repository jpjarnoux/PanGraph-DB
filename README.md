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
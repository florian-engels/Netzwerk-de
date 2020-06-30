#! /bin/bash

# bevor diese Schritte hier ausgeführt werden, muss das Git repository geklont werden
# wir müssen uns im git repository befinden und
# anaconda oder miniconda muss installiert sein

# hier code hin:

#installiere und aktiviere environment
conda env create -f environment.yaml
conda activate pypsa-eur

#installiere solver
conda install -c conda-forge ipopt coincbc

# kopiere die default konfiguration
cp config.default.yaml config.yaml


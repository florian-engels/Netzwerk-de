#! /bin/bash

#installiere und aktiviere environment

conda install -c conda-forge mamba

mamba env create -f environment.yaml
mamba activate pypsa-eur

#installiere solver
mamba install -c conda-forge ipopt coincbc

# kopiere die default konfiguration
cp config.default.yaml config.yaml


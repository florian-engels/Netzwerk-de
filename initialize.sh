#! /bin/bash

#installiere und aktiviere environment
conda env create -f environment.yaml
conda activate pypsa-eur

#installiere solver
conda install -c conda-forge ipopt coincbc

# kopiere die default konfiguration
cp config.default.yaml config.yaml


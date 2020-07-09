#! /bin/bash

#installiere und aktiviere environment

conda install -c conda-forge mamba

mamba env create -f environment.yaml

source $(conda info --base)"/etc/profile.d/conda.sh"
conda activate pypsa-eur

conda install -y -c conda-forge mamba

#installiere solver
mamba install -y -c conda-forge ipopt coincbc

# kopiere die default konfiguration
cp config.default.yaml config.yaml


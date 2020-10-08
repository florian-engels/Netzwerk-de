#! /bin/bash

#gehe zuerst in den repository ordner

#cp config.tutorial.yaml config.yaml

source $(conda info --base)"/etc/profile.d/conda.sh"
conda activate pypsa-eur

# Erzeugen eines 50Knoten Beispielnetzwerks
snakemake --cores #-j 1 results/networks/elec_s_5_ec_lcopt_Co2L-24H.nc

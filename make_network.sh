#! /bin/bash

#gehe zuerst in den repository ordner

cp config.tutorial.yaml config.yaml
conda activate pypsa-eur

# Erzeugen eines 50Knoten Beispielnetzwerks
snakemake -j 1 results/networks/elec_s_50_ec_lcopt_Co2L-24H.nc

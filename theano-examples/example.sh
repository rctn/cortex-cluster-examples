#!/bin/bash
# Job name:
#SBATCH --job-name=theano_test
#
# Partition:
#SBATCH --partition=cortex
#
# Constraint:
#SBATCH --constraint=cortex_fermi
#
# Wall clock limit:
#SBATCH --time=0:0:30
#

## Unload intel compiler so theano falls back to gcc
module unload intel

## Run command
python example.py

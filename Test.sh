#!/bin/bash
#SBATCH --job-name=Testing
#SBATCH --account=nn9305k
#SBATCH --time=10:00:00
#SBATCH --mem-per-cpu=32G

## Set up job environment:
source /cluster/bin/jobsetup

module load Miniconda3/4.4.10
module load prokka/1.7
module load hmmer/3.1b2

source activate Python3p7

time python Annotation.py

source deactivate Python3p7
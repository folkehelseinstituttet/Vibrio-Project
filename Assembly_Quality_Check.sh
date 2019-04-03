#!/bin/bash
#SBATCH --job-name=AsmQC
#SBATCH --account=nn9305k
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=32G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ajkarloss@gmail.com 

## Array Job 
#SBATCH --array=1-6

## Set up job environment:
source /cluster/bin/jobsetup

module load Miniconda3/4.4.10

###################################################
# Assembly Quality Check
###################################################
source activate /work/projects/nn9305k/src/anaconda3/envs/AssemblyQuality
time python bin/Assembly_Quality_Check.py
source deactivate /work/projects/nn9305k/src/anaconda3/envs/AssemblyQuality

###################################################
# Assembly Statistics
###################################################
source activate AssemblyStats
time python bin/Assembly_Statistics.py
source deactivate AssemblyStats

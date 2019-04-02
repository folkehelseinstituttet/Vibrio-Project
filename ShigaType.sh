#!/bin/bash
#SBATCH --job-name=ShigaTyper
#SBATCH --account=nn9305k
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=32G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ajkarloss@gmail.com 

## Array Job 
#SBATCH --array=1-25

## Set up job environment:
source /cluster/bin/jobsetup

module load Miniconda3/4.4.10

## Add the input directory
input_dir="/usit/abel/u1/jeevka/FHI/Data_For_ShigaTyper/02Apr2019/"

ls -l $input_dir | awk '{print $9}' >input.txt
IFS=$'\n' read -d '' -r -a files < input.txt

N1=$((SLURM_ARRAY_TASK_ID*2-1-1)) 
N2=$((SLURM_ARRAY_TASK_ID*2-1))

IF1=${files[$N1]}
IF2=${files[$N2]}

echo "Input File 1: "${files[$N1]}
echo "Input File 2: "${files[$N2]}
    
###################################################
# Check the Quality of Fastq Reads
###################################################
ls -l /usit/abel/u1/jeevka/FHI/Data_For_ShigaTyper/02Apr2019/*.fastq | awk '{print $9}' >input1.txt
IFS=$'\n' read -d '' -r -a TF1 < input1.txt

N1=$((SLURM_ARRAY_TASK_ID*2-1-1)) 
N2=$((SLURM_ARRAY_TASK_ID*2-1))

IF1=${TF1[$N1]}
IF2=${TF1[$N2]}

source activate /work/projects/nn9305k/src/anaconda3/envs/ShigaTyper
time python bin/ShigaTyper.py $IF1 $IF2
source deactivate /work/projects/nn9305k/src/anaconda3/envs/ShigaTyper

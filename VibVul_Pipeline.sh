#!/bin/bash
#SBATCH --job-name=VVFPiplne
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

## Add the input directory
input_dir="/usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/FHI_Data/Fastq_Seq/"

ls -l $input_dir | awk '{print $9}' >input.txt
IFS=$'\n' read -d '' -r -a files < input.txt

N1=$((SLURM_ARRAY_TASK_ID*2-1-1)) 
N2=$((SLURM_ARRAY_TASK_ID*2-1))

IF1=${files[$N1]}
IF2=${files[$N2]}

echo "Input File 1: "${files[$N1]}
echo "Input File 2: "${files[$N2]}

# For running Python scripts
# module load Python/3.5.2-foss-2016b

###################################################
# 1. Remove the adapter sequences
# 2. Remove PhiX genome
###################################################
module load java
time python bin/Clean_Raw_Reads.py $IF1 $IF2 $SLURM_ARRAY_TASK_ID

echo "######################################"
echo "Cleaning RAW reads - DONE"
echo "######################################\n\n"

###################################################
# Check the Quality of Fastq Reads
###################################################
ls -l Trimmed_Fastq_Files/*Trimmed.fastq | awk '{print $9}' >input1.txt
IFS=$'\n' read -d '' -r -a TF1 < input1.txt

N1=$((SLURM_ARRAY_TASK_ID*2-1-1)) 
N2=$((SLURM_ARRAY_TASK_ID*2-1))

IF1=${TF1[$N1]}
IF2=${TF1[$N2]}

echo "Input File 1: "${TF1[$N1]}
echo "Input File 2: "${TF1[$N2]}

###################################################
# Check the Quality of Fastq Reads
###################################################
source activate KmerID
time python bin/Species_Confirmation.py $IF1 $IF2
source deactivate KmerID

echo "#####################################"
echo "Executing KmerID ....DONE"
echo "#####################################\n\n"

###################################################
# Denova Assembly 
###################################################
source activate Spades
time python bin/Denova_Assembly.py $IF1 $IF2
source deactivate Spades

echo "##################################"
echo " Denova Assembly.....Done"
echo "##################################"

###################################################
# Reference Mapping
###################################################
source activate /work/projects/nn9305k/src/anaconda3/envs/ReferenceMapping
time python bin/Reference_Mapping.py $IF1 $IF2
source deactivate /work/projects/nn9305k/src/anaconda3/envs/ReferenceMapping

echo "##################################"
echo " Reference Mapping.....Done"
echo "##################################"

###################################################
# Genome Annotation
###################################################
source activate GenomeAnnotation
time python bin/Annotation.py
source deactivate GenomeAnnotation

echo "##################################"
echo "Genome Annotation .....Done"
echo "##################################"

###################################################
# Anti-microbial resistance genes
###################################################
# Preparing the AMR Database
# ariba getref card out.card
# ariba prepareref -f /cluster/home/jeevka/out.card.fa -m /cluster/home/jeevka/out.card.tsv /usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/CARD_DB

source activate ARIBA
time python bin/AMR.py $IF1 $IF2
source deactivate ARIBA

echo "##################################"
echo "AMR mapping.....Done"
echo "##################################"

###################################################
# Phylogenetic Tree
###################################################
source activate Python3p7
time python bin/Phylogenetics.py
source deactivate Python3p7

echo "##################################"
echo "Phylogenetics Tree.....Done"
echo "##################################"

###################################################
# Serotyping : SeqSero 1.0 for Salmonella
###################################################
source activate SeqSero
time python bin/Serotyping.py $IF1 $IF2
source deactivate SeqSero

echo "##################################"
echo " Serotyping.....Done"
echo "##################################"

###################################################
# cgMLST - Using ARIBA PubMLST
###################################################
# Preparing the PubMLST Reference
# ariba pubmlstget "Vibrio Vulnificus" get_mlst

source activate ARIBA
time python bin/cgMLST.py $IF1 $IF2
source deactivate ARIBA

echo "##################################"
echo "cgMLST .....Done"
echo "##################################"

###################################################
# AMRT_Virulance Genes using ABRICATE
###################################################
source activate ABRicate
time python bin/AMR_Virulence.py $IF1 $IF2
source deactivate ABRicate

echo "##################################"
echo "AMR-Virulance Gene Mapping.....Done"
echo "##################################"

<< --MULTILINE-COMMENT--
###################################################
# ResFinder - Resistance genes finder
###################################################
source activate ResFinder
time python ResFinder.py $IF1 $IF2
source deactivate ResFinder

echo "##################################"
echo "ResFinder.....Done"
echo "##################################"

###################################################
# PlasmidFinder - Plasmid Finder 
###################################################
source activate PlasmidFinder
time python PlasmidFinder.py $IF1 $IF2
source deactivate PlasmidFinder

echo "##################################"
echo "PlasmidFinder.....Done"
echo "##################################"

###################################################
# VirulanceFinder - Virulance genes finder
###################################################
source activate VirulanceFinder
time python VirulanceFinder.py $IF1 $IF2
source deactivate VirulanceFinder

echo "##################################"
echo "VirulanceFinder.....Done"
echo "##################################"

###################################################
# PointFinder - Detecting mutations in chromosomes
###################################################
source activate PointFinder
time python PointFinder.py $IF1 $IF2
source deactivate PointFinder

echo "##################################"
echo "PointFinder mapping.....Done"
echo "##################################"

--MULTILINE-COMMENT--

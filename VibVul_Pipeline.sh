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

##output_dir="/usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/FHI_Data/Vibrio/FastQC_Outputs/"
## echo "Hello : "$SLURM_ARRAY_TASK_ID

# For bbduk 
module load java

# For running Python scripts
# module load Python/3.5.2-foss-2016b

###################################################
# STEP 1
# 1. Remove the adapter sequences
# 2. Remove PhiX genome
###################################################

echo "######################################"
echo "Cleaning RAW reads"
echo "######################################\n\n"

# time python bin/Clean_Raw_Reads.py $IF1 $IF2 $SLURM_ARRAY_TASK_ID

echo "######################################"
echo "Cleaning RAW reads - DONE"
echo "######################################\n\n"


###################################################
# STEP 2
# Check the Quality of Fastq Reads
###################################################
module load fastqc/0.11.2
module load Anaconda3/5.1.0

echo "#####################################"
echo "Executing FastQC ...."
echo "#####################################\n\n"

ls -l Trimmed_Fastq_Files/*Trimmed.fastq | awk '{print $9}' >input1.txt
IFS=$'\n' read -d '' -r -a TF1 < input1.txt

N1=$((SLURM_ARRAY_TASK_ID*2-1-1)) 
N2=$((SLURM_ARRAY_TASK_ID*2-1))

IF1=${TF1[$N1]}
IF2=${TF1[$N2]}

echo "Input File 1: "${TF1[$N1]}
echo "Input File 2: "${TF1[$N2]}

<< --MULTILINE-COMMENT--
# Activating MultiQC Conda
source activate MultiQC

#time python bin/Quality_Check.py $IF1 $IF2

# Deactivate the MUltiQC Conda
source deactivate MultiQC

echo "#####################################"
echo "Executing FastQC ....DONE"
echo "#####################################\n\n"

###################################################
# STEP 2
# Check the Quality of Fastq Reads
###################################################

echo "#####################################"
echo "Executing KmerID ...."
echo "#####################################\n\n"

source activate KmerID

#time python bin/Species_Confirmation.py $IF1 $IF2

source deactivate KmerID

echo "#####################################"
echo "Executing KmerID ....DONE"
echo "#####################################\n\n"

###################################################
# STEP 3
# Denova Assembly 
###################################################

#module load spades/3.9.0

source activate Spades

#time python bin/Denova_Assembly.py $IF1 $IF2

source deactivate Spades

###################################################
# STEP 4
# Reference Mapping
###################################################

module load bowtie2/2.3.1
module load Python/3.5.2-foss-2016b

time python bin/Reference_Mapping.py $IF1 $IF2

###################################################
# STEP 5
# Assembly Corrections
###################################################

#time python bin/Assembly_Corrections.py

###################################################
# STEP 6
# Assembly Corrections
###################################################

module load quast/4.6.0
source activate Python3p7

time python bin/Assembly_Quality_Check.py

source deactivate Python3p7

###################################################
# STEP 7
# Assembly Statistics
###################################################

source activate AssemblyStats

time python bin/Assembly_Statistics.py

source deactivate AssemblyStats



###################################################
# STEP 8
# Genome Annotation
###################################################
module load prokka/1.7
module load hmmer/3.1b2

source activate Python3p7

time python bin/Annotation.py

source deactivate Python3p7

###################################################
# STEP 9
# Anti-microbial resistance genes
###################################################
# Preparing the AMR Database
# ariba getref card out.card
# ariba prepareref -f /cluster/home/jeevka/out.card.fa -m /cluster/home/jeevka/out.card.tsv /usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/CARD_DB

source activate ARIBA

time python bin/AMR.py $IF1 $IF2

source deactivate ARIBA


###################################################
# STEP 10
# Phylogenetic Tree
###################################################
source activate Python3p7

time python bin/Phylogenetics.py

source deactivate Python3p7

--MULTILINE-COMMENT--
###################################################
# STEP 11
# Serotyping : SeqSero 1.0 for Salmonella
###################################################

source activate SeqSero

time python bin/Serotyping.py $IF1 $IF2

source deactivate SeqSero

###################################################
# STEP 12
# cgMLST - Using ARIBA PubMLST
###################################################
# Preparing the PubMLST Reference
# ariba pubmlstget "Vibrio Vulnificus" get_mlst

<< --MULTILINE-COMMENT--

source activate ARIBA

time python bin/cgMLST.py $IF1 $IF2

source deactivate ARIBA

###################################################
# STEP 13
# AMRT_Virulance Genes using ABRICATE
###################################################

source activate ABRicate

time python bin/AMR_Virulence.py $IF1 $IF2

source deactivate ABRicate

--MULTILINE-COMMENT--

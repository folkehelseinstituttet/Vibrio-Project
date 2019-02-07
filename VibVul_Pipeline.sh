#!/bin/bash
#SBATCH --job-name=VVFPiplne
#SBATCH --account=nn9305k
#SBATCH --time=10:00:00
#SBATCH --mem-per-cpu=32G

## Set up job environment:
source /cluster/bin/jobsetup

module load Miniconda3/4.4.10
 
# For bbduk 
module load java

# For running Python scripts
# module load Python/3.5.2-foss-2016b

###################################################
# STEP 1
# 1. Remove the adapter sequences
# 2. Remove PhiX genome
###################################################

time python Clean_Raw_Reads.py

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

# Activating MultiQC Conda
source activate MultiQC

time python Quality_Check.py

# Deactivate the MUltiQC Conda
source deactivate MultiQC

###################################################
# STEP 3
# Denova Assembly 
###################################################

#module load spades/3.9.0

source activate Spades

time python Denova_Assembly.py

source deactivate Spades

###################################################
# STEP 4
# Reference Mapping
###################################################
<< --MULTILINE-COMMENT--

module load bowtie2/2.3.1
module load Python/3.5.2-foss-2016b

time python Reference_Mapping.py

###################################################
# STEP 5
# Assembly Corrections
###################################################

#time python Assembly_Corrections.py

###################################################
# STEP 6
# Assembly Corrections
###################################################

module load quast/4.6.0
source activate Python3p7

time python Assembly_Quality_Check.py

source deactivate Python3p7

--MULTILINE-COMMENT--
###################################################
# STEP 7
# Assembly Statistics
###################################################

source activate AssemblyStats

time python Assembly_Statistics.py

source deactivate AssemblyStats

###################################################
# STEP 8
# Genome Annotation
###################################################
module load prokka/1.7
module load hmmer/3.1b2

source activate Python3p7

time python Annotation.py

source deactivate Python3p7

###################################################
# STEP 9
# Anti-microbial resistance genes
###################################################
# Preparing the AMR Database
# ariba getref card out.card
# ariba prepareref -f /cluster/home/jeevka/out.card.fa -m /cluster/home/jeevka/out.card.tsv /usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/CARD_DB

source activate ARIBA

time python AMR.py

source deactivate ARIBA

###################################################
# STEP 10
# Phylogenetic Tree
###################################################
source activate Python3p7

time python Phylogenetics.py

source activate Python3p7

<< --MULTILINE-COMMENT-- 
###################################################
# STEP 11
# Serotyping : SeqSero 1.0 for Salmonella
###################################################

time python Serotyping.py
--MULTILINE-COMMENT--

###################################################
# STEP 12
# cgMLST - Using ARIBA PubMLST
###################################################
# Preparing the PubMLST Reference
# ariba pubmlstget "Vibrio Vulnificus" get_mlst

source activate ARIBA

time python cgMLST.py

source deactivate ARIBA

###################################################
# STEP 13
# AMRT_Virulance Genes using ABRICATE
###################################################
source activate ABRicate

time python AMR_Virulence.py

source deactivate ABRicate
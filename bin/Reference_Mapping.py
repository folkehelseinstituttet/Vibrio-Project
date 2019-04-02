import re
import sys
import configparser
import os

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

file_location = config['BASIC']['FASTQ_FILES']
ref_genome = config['BASIC']['REF_GENOME']

fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Create output folder
if not os.path.exists("Reference_Mapped_Files"):
    os.makedirs("Reference_Mapped_Files")

#for i in range(0,len(fastq_files),2):

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

# Input Files
#INF1 = file_location + fastq_files[i]
#INF2 = file_location + fastq_files[i+1]

IN = SF.get_file_name(INF1)

OF = "Reference_Mapped_Files/" + IN
execute_bowtie2 = "bowtie2 --sensitive -p 30 -x " + ref_genome + " -1 " + INF1 + "-2 " + INF2 + " -S " + OF + ".sam"
os.system(execute_bowtie2)

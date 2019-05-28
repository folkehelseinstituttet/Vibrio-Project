from os import listdir
import sys
import re
import os
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

# Trimmed FastQ Files
file_location = "Trimmed_Fastq_Files"

fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]
dir_name = sys.argv[3]


if dir_name == "FastQC_Reports_Before_Cleaning":
    fastq_location = config['BASIC']['FASTQ_FILES']
    IF1 = fastq_location + "/" + INF1
    IF2 = fastq_location + "/" + INF2
else:
    IF1 = INF1
    IF2 = INF2
    pass



# Create Main output folder
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    
#for i in range(len(fastq_files)):

# Create output report folder for each sample
print ("FastQC: Quality Checking ....:", IF1)
execute_fastQC = "fastqc -q " + IF1 +" -o " + dir_name + "/"
os.system(execute_fastQC)

print ("FastQC: Quality Checking ....:", IF2)
execute_fastQC = "fastqc -q " + IF2 +" -o " + dir_name + "/"
os.system(execute_fastQC)

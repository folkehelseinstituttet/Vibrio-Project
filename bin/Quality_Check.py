from os import listdir
import sys
import re
import os

# User defined modules
import Sub_Functions as SF

# Trimmed FastQ Files
file_location = "Trimmed_Fastq_Files"

fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]
dir_name = sys.argv[3]

# Create Main output folder
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    
#for i in range(len(fastq_files)):

# Create output report folder for each sample
print ("Qulity Checking ....:", INF1)
print ("Qulity Checking ....:", INF2)

execute_fastQC = "fastqc -q " + INF1 +" -o " + dir_name + "/"
os.system(execute_fastQC)

execute_fastQC = "fastqc -q " + INF2 +" -o " + dir_name + "/"
os.system(execute_fastQC)


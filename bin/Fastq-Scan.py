from os import listdir
import sys
import re
import os
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

genome_size = config['BASIC']['REF_GENOME_SIZE']

# Input Files
IF1 = sys.argv[1]
IF2 = sys.argv[2]
dir_name = sys.argv[3]

if dir_name == "FastQ_Stats_Before_Cleaning":
    fastq_location = fastq_location = config['BASIC']['FASTQ_FILES']
    IF1 = fastq_location + "/" + IF1
    IF2 = fastq_location + "/" + IF2
else:
    pass
    #fastq_location = "Trimmed_Fastq_Files"

# Create Main output folder
if not os.path.exists(dir_name):
    os.makedirs(dir_name)   

IN = SF.get_file_name(IF1)

IN = IN.split(".")[0] + ".fasta"
OF = dir_name + "/" + IN.split(".")[0]

print("Fastq-Scan:", IF1)    
execute_fastq_scan = "cat " + IF1 + " | fastq-scan -g " + genome_size + " >" + OF
os.system(execute_fastq_scan)

print("Fastq-Scan:", IF2)
execute_fastq_scan = "cat " + IF2 + " | fastq-scan -g " + genome_size + " >" + OF
os.system(execute_fastq_scan)
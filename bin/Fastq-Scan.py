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

# Create Main output folder
if not os.path.exists(dir_name):
    os.makedirs(dir_name)   

IN = SF.get_file_name(IF1)

IN = IN.split(".")[0] + ".fasta"
OF = dir_name + "/" + IN.split(".")[0]
    
execute_fastq_scan = "cat " + IF1 + " | fastq-scan -g " + genome_size + " >" + OF
os.system(execute_fastq_scan)

execute_fastq_scan = "cat " + IF2 + " | fastq-scan -g " + genome_size + " >" + OF
os.system(execute_fastq_scan)
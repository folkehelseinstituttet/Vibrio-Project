import re
import os
import sys
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

# Create reference databases
# python setup_refs.py -n vibrio_vulnificus -f References/ -c config/config.cnf

file_location = config['BASIC']['FASTQ_FILES']
kmerID_loc = config['KmerID']['kmerID_location']
kmerID_DB = config['KmerID']['kmerID_database']
# Call to import the Paired end files
fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

kmer_reports = "KmerID_Reports/"

# Create another folder to store the assembly reports
if not os.path.exists("KmerID_Reports"):
    os.makedirs("KmerID_Reports")

for i in range(0,len(fastq_files),2):
    IF1 = file_location + fastq_files[i]
    IF2 = file_location + fastq_files[i+1]
    OF1 = "KmerID_Reports/" + fastq_files[i] + "_out"
    OF2 = "KmerID_Reports/" + fastq_files[i+1] + "_out"
    kmer = KmerID_loc + "/kmerid.py" 
    execute_kmerID = "python " + "kmer -f " + IF1 + " --config=" + KmerID_loc + "config/config.cnf -n >" + OF1
    os.system(execute_kmerID)
    
    execute_kmerID = "python " + "kmer -f " + IF2 + " --config=" + KmerID_loc + "config/config.cnf -n >" + OF2
    os.system(execute_kmerID)
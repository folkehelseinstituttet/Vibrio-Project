import re
import os
import sys
import ConfigParser

# User defined modules
import Sub_Functions as SF

config = ConfigParser.ConfigParser()
config.read("config.ini")

# Create reference databases
# python setup_refs.py -n vibrio_vulnificus -f References/ -c config/config.cnf

file_location = config.get('BASIC','FASTQ_FILES')
kmerID_loc = config.get('KmerID','kmerID_location')
kmerID_DB = config.get('KmerID','kmerID_database')

# Call to import the Paired end files
fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

kmer_reports = "KmerID_Reports/"
current_location = os.getcwd()

# Create another folder to store the assembly reports
if not os.path.exists("KmerID_Reports"):
    os.makedirs("KmerID_Reports")

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

INF1 = SF.get_file_name(INF1)
INF2 = SF.get_file_name(INF2)

INF1 = file_location + INF1
INF2 = file_location + INF2

output_location = current_location + "/KmerID_Reports/"

OF1 = output_location + INF1 + "_out"
OF2 = output_location + INF2 + "_out"

os.chdir(kmerID_loc)
kmer = "kmerid.py" 

execute_kmerID = "python " + kmer + " -f " + INF1 + " --config=" + "config/config.cnf -n >" + OF1
os.system(execute_kmerID)
    
execute_kmerID = "python " + kmer + " -f " + INF2 + " --config=" + "config/config.cnf -n >" + OF2
os.system(execute_kmerID)

os.chdir(current_location)

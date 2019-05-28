import re
import os
import sys
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

kraken_DB = config['Kraken2']['Kraken2_DB_location']
kraken2 = config['Kraken2']['Kraken2_location']


kraken2_reports = "Kraken2_Reports/"

current_location = os.getcwd()

# Create another folder to store the AMR reports
if not os.path.exists("Kraken2_Reports"):
    os.makedirs("Kraken2_Reports")
    
# Call to import the Paired end files
# fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

IN = SF.get_file_name(INF1)

#for i in range(0,len(fastq_files),2):
#IF1 = file_location + fastq_files[i]
#IF2 = file_location + fastq_files[i+1]
kraken2_reports_directory = kraken2_reports + IN.split(".")[0]

#if os.path.exists(kraken2_reports_directory):
#    os.rmdir(kraken2_reports_directory)

execute_kraken2 = bracken + " --db " + kraken_DB + " threads 20 --paired " + INF1 + " " + INF2 + " >" + kraken2_reports_directory
os.system(execute_kraken2)

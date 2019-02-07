import re
import os
import sys
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

ARIBA_PubMLST_location = config['MLST']['MLST_DB_LOCATION']
file_location = config['BASIC']['FASTQ_FILES']

MLST_reports = "cgMLST/"

# Create another folder to store the assembly reports
if not os.path.exists("cgMLST"):
    os.makedirs("cgMLST")

# Call to import the Paired end files
fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

for i in range(0,len(fastq_files),2):
    IF1 = file_location + fastq_files[i]
    IF2 = file_location + fastq_files[i+1]
    MLST_reports_file = MLST_reports + fastq_files[i].split(".")[0]
    execute_ariba_MLST = "ariba run " + ARIBA_PubMLST_location + " " + IF1 + " " + IF2 + " " + MLST_reports_file
    os.system(execute_ariba_MLST)


# Make the summary-reports from all the runs
# e.x. ariba summary out.summary out.run1/report1.tsv out.run2/report2.tsv out.run3/report3.tsv

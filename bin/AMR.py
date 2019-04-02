import re
import os
import sys
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

AMR_DB = config['AMR']['AMR_DATABASE']
file_location = config['BASIC']['FASTQ_FILES']

amr_reports = "AMR/"

current_location = os.getcwd()

# Create another folder to store the assembly reports
#if not os.path.exists(current_location + "AMR"):
#    os.makedirs(current_location"AMR")
    
# Call to import the Paired end files
fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Input Files
INF1 = file_location + sys.argv[1]
INF2 = file_location + sys.argv[2]

IN = SF.get_file_name(INF1)

#for i in range(0,len(fastq_files),2):
#IF1 = file_location + fastq_files[i]
#IF2 = file_location + fastq_files[i+1]
amr_reports_directory = amr_reports + IN.split(".")[0]

if os.path.exists(amr_reports_directory):
    os.rmdir(amr_reports_directory)

execute_ariba = "ariba run " + AMR_DB + " " + INF1 + " " + INF2 + " " + amr_reports_directory
os.system(execute_ariba)


# Make the summary-reports from all the runs
# e.x. ariba summary out.summary out.run1/report1.tsv out.run2/report2.tsv out.run3/report3.tsv

import re
import os
import sys
import shutil
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

PF_loc = config['PlasmidFinder']['PlasmidFinder']
DB = config['PlasmidFinder']['PlasmidFinder_DB']

# User defined modules
import Sub_Functions as SF

# Trimmed FastQ Files
file_location = "Trimmed_Fastq_Files"

# Create Main output folder
if not os.path.exists("PlasmidFinder_Output"):
    os.makedirs("PlasmidFinder_Output")
    
# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

INF1 = SF.get_file_name(INF1)
INF2 = SF.get_file_name(INF2)
    
# PlasmidFinder
print ("Excuting PlasmidFinder....:", INF1,"\t",INF2)
os.system("source activate PlasmidFinder")
execute_plasmidfinder = PF_loc + "plasmidfinder.py -1 Trimmed_Fastq_Files/" + INF1 + " -2 Trimmed_Fastq_Files/" + INF2 + " -t 5 -o " + Output_Folder    
os.system(execute_plasmidfinder)
os.system("source deactivate PlasmidFinder")
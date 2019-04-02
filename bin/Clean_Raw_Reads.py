from os import listdir
import sys
import re
import os
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

file_location = config['BASIC']['FASTQ_FILES']
phix_location = config['BASIC']['PHIX_GENOME']
adapter_location = config['BASIC']['ADAPTER_FILE']

# Call to import the Paired end files
fastq_files = SF.list_paird_end_files(file_location)

bbduck = "/usit/abel/u1/jeevka/FHI/Vibrio_Project_2018/Vibrio_vulnificus/Pipelines/bbmap/bbduk.sh"

# Create output folder
if not os.path.exists("Trimmed_Fastq_Files"):
    os.makedirs("Trimmed_Fastq_Files")

#for i in range(0,len(fastq_files),2):

# Input Files
INF1 = file_location + sys.argv[1]
INF2 = file_location + sys.argv[2]
LogFile = sys.argv[3]
    
# Output Files
OF1 = "Trimmed_Fastq_Files/" + sys.argv[1].split(".")[0] + "_Trimmed.fastq" 
OF2 = "Trimmed_Fastq_Files/" + sys.argv[2].split(".")[0] + "_Trimmed.fastq"
log_file = "Trimmed_Fastq_Files/" + LogFile + ".log"
    
print ("Executing bbduk for..", INF1,"\t",INF2,"\n")
   
exec_bbduck = bbduck + " threads=5 ref=" + phix_location + "," + adapter_location + " in1=" + INF1 + " in2=" + INF2 + " out=" + OF1 + " out2=" + OF2 + " k=31 ktrim=r mink=11 hdist=1 tbo=f tpe=f qtrim=r trimq=15 maq=15 minlen=36 forcetrimright=149 stats=stats.txt &> " + log_file
os.system(exec_bbduck)
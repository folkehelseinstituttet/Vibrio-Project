from os import listdir
import sys
import re
import os
import ConfigParser

# User defined modules
import Sub_Functions as SF

config = ConfigParser.ConfigParser()
config.read("config.ini")

seqsero_location = config.get('TOOL_LOCATION','SEQSERO')
fastq_location = config.get('BASIC','FASTQ_FILES')
assembly_location = "Denova_Assemblies/Final_Assemblies/"

# Create Main output folder
if not os.path.exists("Serotyping"):
    os.makedirs("Serotyping")

# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

IN = SF.get_file_name(INF1)
    
#for i in asm_files:
IF = assembly_location + INF1
OF = "Serotyping/" + IN.split(".")[0]
if not os.path.exists(OF):
    os.makedirs(OF)

OF1 = "Serotyping/" + IN.split(".")[0] + "/" + IN.split(".")[0] + "_1.txt" 
OF2 = "Serotyping/" + IN.split(".")[0] + "/" + IN.split(".")[0] + "_2.txt"

#execute_seqsero = seqsero_location + "/SeqSero.py -m 4 -i " + IF + " -b mem"
execute_seqsero = seqsero_location + "SeqSero.py -m 1 -i " + INF1 + " -b mem >" + OF1
os.system(execute_seqsero)

execute_seqsero = seqsero_location + "SeqSero.py -m 1 -i " + INF2 + " -b mem >" + OF2
os.system(execute_seqsero)
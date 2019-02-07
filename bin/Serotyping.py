from os import listdir
import sys
import re
import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

seqsero_location = config['TOOL_LOCATION']['SEQSERO']
assembly_location = "Denova_Assemblies/Final_Assemblies/"

# Create Main output folder
if not os.path.exists("Serotyping"):
    os.makedirs("Serotyping")
    
for i in asm_files:
    IF = assembly_location + i
    OF = "Serotyping/" + i.split(".")[0]
    if not os.path.exists(OF):
        os.makedirs(OF)
    
    execute_seqsero = "SeqSero.py -m 4 -i " + IF + " -b mem"
    os.system(execute_seqsero)

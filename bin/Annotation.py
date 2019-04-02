from os import listdir
import sys
import re
import os
#import ConfigParser

# User defined modules
import Sub_Functions as SF

assembly_location = "Denova_Assemblies/Final_Assemblies/"

# Call to import the Paired end files
asm_files = SF.list_paird_end_files(assembly_location)

# Create Main output folder
if not os.path.exists("Annotation"):
    os.makedirs("Annotation")

for i in asm_files:
    IF = assembly_location + i
    OF = "Annotation/" + i.split(".")[0]
    if not os.path.exists(OF):
        os.makedirs(OF)
    
    execute_prokka = "prokka --outdir " + OF + " --addgenes --force --prefix Annotatted " + IF + " --kingdom Bacteria"
    os.system(execute_prokka)
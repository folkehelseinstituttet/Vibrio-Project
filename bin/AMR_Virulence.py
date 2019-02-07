from os import listdir
import sys
import re
import os
import configparser

# User defined modules
import Sub_Functions as SF

assembly_location = "Denova_Assemblies/Final_Assemblies/"

# Call to import the Paired end files
asm_files = SF.list_paird_end_files(assembly_location)

# Create Main output folder
if not os.path.exists("AMR_Virulence_Abricate"):
    os.makedirs("AMR_Virulence_Abricate")   

for i in asm_files:
    IF = assembly_location + i
    OF = "AMR_Virulence_Abricate/" + i.split(".")[0]
    #if not os.path.exists(OF):
    #    os.makedirs(OF)
    
    execute_abricate = "abricate " + IF + " >" + OF
    os.system(execute_abricate)
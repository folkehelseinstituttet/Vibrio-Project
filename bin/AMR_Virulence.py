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

# Input Files
IF1 = sys.argv[1]
IF2 = sys.argv[2]

IN = SF.get_file_name(IF1)

IN = IN.split(".")[0] + ".fasta"
IF = assembly_location + IN
OF = "AMR_Virulence_Abricate/" + IN.split(".")[0]
#if not os.path.exists(OF):
#    os.makedirs(OF)
    
execute_abricate = "abricate " + IF + " >" + OF
os.system(execute_abricate)
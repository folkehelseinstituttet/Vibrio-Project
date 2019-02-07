import re
import os
import sys
import configparser

# User defined modules
import Sub_Functions as SF

config = configparser.ConfigParser()
config.read("config.ini")

assembly_location = "Denova_Assemblies/Final_Assemblies/"
assembly_statistics = "Denova_Assemblies/Assembly_Statistics/"

# Create another folder to store the assembly reports
if not os.path.exists("Denova_Assemblies/Assembly_Statistics/"):
    os.makedirs("Denova_Assemblies/Assembly_Statistics/")

# Call to import the Paired end files
asm_files = SF.list_paird_end_files(assembly_location)

for i in asm_files:
    asm_file = assembly_location + i
    OF = assembly_statistics + i + ".statistics"
    execute_asm_stat = "assembly-stats" + " " + asm_file + " >" + OF 
    os.system(execute_asm_stat)
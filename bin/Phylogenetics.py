import re
import os
import sys
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ref_genome = config['BASIC']['REF_GENOME']
parsnp_location = config['TOOL_LOCATION']['PARSNP']

assembly_location = "Denova_Assemblies/Final_Assemblies/"
phylogenetics_reports = "Phylogenetics_Reports/"

# Create another folder to store the assembly reports
if not os.path.exists("Phylogenetics_Reports"):
    os.makedirs("Phylogenetics_Reports")

execute_parsnp = parsnp_location + "parsnp -r " + ref_genome + " -d " + assembly_location + " -o " + phylogenetics_reports + " -p 8"
os.system(execute_parsnp)
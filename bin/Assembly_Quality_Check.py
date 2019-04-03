import re
import os
import sys
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ref_genome = config['BASIC']['REF_GENOME']
quast = config['TOOL_LOCATION']['QUAST']

assembly_location = "Denova_Assemblies/Final_Assemblies/*"
assembly_reports = "Denova_Assemblies/Assembly_Reports/"

# Create another folder to store the assembly reports
if not os.path.exists("Denova_Assemblies/Assembly_Reports"):
    os.makedirs("Denova_Assemblies/Assembly_Reports")

execute_quast = quast + " " + assembly_location + " -o " + assembly_reports + " -r " + ref_genome
os.system(execute_quast)


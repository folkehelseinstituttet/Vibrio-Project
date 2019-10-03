import re
import os
import sys
import shutil

# User defined modules
import Sub_Functions as SF

# Trimmed FastQ Files
file_location = "Trimmed_Fastq_Files"

fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Create Main output folder
if not os.path.exists("Denova_Assemblies"):
    os.makedirs("Denova_Assemblies")

# Create another folder to copy the final assemblies
if not os.path.exists("Denova_Assemblies/Final_Assemblies"):
    os.makedirs("Denova_Assemblies/Final_Assemblies")
    
#for i in range(0,len(fastq_files),2):
    
# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

INF1 = SF.get_file_name(INF1)
INF2 = SF.get_file_name(INF2)

# Output Folders
Output_Folder = "Denova_Assemblies/" + INF1.split(".")[0]

if not os.path.exists(Output_Folder):
    os.makedirs(Output_Folder)
    
# Denova Assembly using SPADES
print ("Assembling using....:", INF1,"\t",INF2)
execute_spades = "spades.py -1 Trimmed_Fastq_Files/" + INF1 + " -2 Trimmed_Fastq_Files/" + INF2 + " -t 5 -o " + Output_Folder
    
os.system(execute_spades)
    
# Copying and Renaming the scaffolds.fasta files to one folder
source_file = Output_Folder + "/scaffolds.fasta"
shutil.copy2(source_file,"Denova_Assemblies/Final_Assemblies/")

os.rename("Denova_Assemblies/Final_Assemblies/scaffolds.fasta", "Denova_Assemblies/Final_Assemblies/"  + INF1.split(".")[0] + ".fasta")
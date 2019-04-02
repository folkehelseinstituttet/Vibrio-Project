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
if not os.path.exists("ShigaType_Output"):
    os.makedirs("ShigaType_Output")
    
# Input Files
INF1 = sys.argv[1]
INF2 = sys.argv[2]

INF1 = SF.get_file_name(INF1)
INF2 = SF.get_file_name(INF2)

# Output Folders
Output_File = "ShigaType_Output/" + INF1.split(".")[0]

#if not os.path.exists(Output_Folder):
#    os.makedirs(Output_Folder)

shigatyper = "/work/projects/nn9305k/src/ShigaTyper/shigatyper/shigatyper/shigatyper.py"
fastq = "/usit/abel/u1/jeevka/FHI/Data_For_ShigaTyper/02Apr2019/"

# Denova Assembly using Shigatyper
execute_shigatyper = "python " + shigatyper + " " + fastq + INF1 + " " + fastq +  INF2 + " >" + Output_File 
os.system(execute_shigatyper)
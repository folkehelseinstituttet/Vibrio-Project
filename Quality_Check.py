from os import listdir
import sys
import re
import os

# User defined modules
import Sub_Functions as SF

# Trimmed FastQ Files
file_location = "Trimmed_Fastq_Files"

fastq_files = SF.list_paired_end_files_with_pattern(file_location,"*.fastq")

# Create Main output folder
if not os.path.exists("FastQC_Reports"):
    os.makedirs("FastQC_Reports")

for i in range(len(fastq_files)):
    
    # Create output report folder for each sample
    print ("Qulity Checking ....:", fastq_files[i])
    
    execute_fastQC = "fastqc -q " + file_location + "/" + fastq_files[i] +" -o " + "FastQC_Reports/"
    os.system(execute_fastQC)

# Executing MultiQC
execute_multiQC = "multiqc --force FastQC_Reports"
os.system(execute_multiQC)


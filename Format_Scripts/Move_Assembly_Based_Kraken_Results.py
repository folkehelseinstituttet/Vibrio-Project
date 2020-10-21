import sys
import re
import os
import shutil

kraken_file = open(sys.argv[1],"r")
data = kraken_file.readlines()

species_samples = {}
for i in data:
    temp = i.split(",")
    species_samples[temp[1]] = temp[2].strip()

Asm_Location = "Denova_Shovill_Assembly/Trimmed_Fastq_Files"

for i in species_samples:
    if not os.path.exists(species_samples[i]):
        fname1 = i.split("_Reports")[0]+ ".fastq"
        src_loc = Asm_Location + "/" + fname1 + "/contigs.fa"
        asm_file_name = fname1.split(".")[0]
        dst_loc = species_samples[i] + "/" + asm_file_name + ".fa"
        print (src_loc)
        print (dst_loc)
        
        shutil.copy2(src_loc,dst_loc)
    
    else:
        fname1 = i.split("_Reports")[0]+ ".fastq"
        src_loc = Asm_Location + "/" + fname1 + "/contigs.fa"
        asm_file_name = fname1.split(".")[0]
        dst_loc = species_samples[i] + "/" + asm_file_name + ".fa"
        print (src_loc)
        print (dst_loc)
        shutil.copy2(src_loc,dst_loc)
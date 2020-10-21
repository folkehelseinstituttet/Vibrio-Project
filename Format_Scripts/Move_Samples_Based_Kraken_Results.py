import sys
import re
import os
import shutil

def find_file_name(fname1):
    if re.search("_R1_",fname1):
        fname2 = fname1.replace("R1","R2")
    elif re.search("_1_",fname1):
        fname2 = fname1.replace("_1_","_2_")

    return fname2


kraken_file = open(sys.argv[1],"r")
data = kraken_file.readlines()

species_samples = {}
for i in data:
    temp = i.split(",")
    species_samples[temp[1]] = temp[2].strip()

#print (species_samples)

Fastq_Location = "Trimmed_Fastq_Files"

for i in species_samples:
    if not os.path.exists(species_samples[i]):
        #os.makedirs(species_samples[i])
        fname1 = i.split("_Reports")[0] + ".fastq"
        fname2 = find_file_name(fname1)
        file1 = Fastq_Location + "/" + fname1
        file2 = Fastq_Location + "/" + fname2
        print (file1)
        print (file2)
        
        shutil.copy2(file1,species_samples[i])
        shutil.copy2(file2,species_samples[i])
    else:
        fname1 = i.split("_Reports")[0] + ".fastq"
        fname2 = find_file_name(fname1)
        file1 = Fastq_Location + "/" + fname1
        file2 = Fastq_Location + "/" + fname2
        print (file1)
        print (file2)
        
        shutil.copy2(file1,species_samples[i])
        shutil.copy2(file2,species_samples[i])
    
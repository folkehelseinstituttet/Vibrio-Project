from os import listdir
import re
import os
import shutil

file_location = "/cluster/home/jeevka/2019_Oct_Vibrio/Denova_Shovill_Assembly/"

asm_files_list = [f for f in listdir(file_location)]

for i in asm_files_list:
    fname = file_location + i + "/contigs.fa"
    ftype = i.replace("fastq","fa")
    newfname = "/cluster/home/jeevka/2019_Oct_Vibrio/Denova_Assemblies_Final_Dec2019/" + ftype
    print (fname,newfname)
    try:
        shutil.copy(fname,newfname)
    except:
        print (fname)

import sys
import re
import os, errno
import shutil

F1 = open("Kraken2_Results_Dec2019.csv","r")
file_species = {}

asm_location = "Denova_Assemblies_Final_Dec2019/"

for  i in F1:
    temp = i.split(",")
    file_species[temp[1]] = temp[2].strip()
    
    # Creating the Species folders
    """
    try:
        os.mkdir(temp[2].strip())
    except:
        print ("Folder ", temp[2].strip()," exists")
    """    
    asm_file = asm_location + temp[1] + ".fa"
    shutil.copy2(asm_file,temp[2].strip())
    
    print (asm_file)    

import re
import sys
import os
from os import listdir

def pick_results(F,SID):
    for i in F:
        if re.search("^O antigen",i):
            temp = i.split()

        if re.search("Predicted antigenic profile",i):
            temp1 = i.split()[3]
        
        if re.search("Predicted serotype",i):
            temp2 = i.split(":")[1]
        
        if re.search("antigen prediction",i):
            temp3 = i.split(":")[1]
        
        if re.search("^H1",i):
            temp4 = i.split(":")[1]
            
        if re.search("^H2",i):
            temp5 = i.split(":")[1]
            
    print(SID,"\t",temp[3],"\t",temp3.strip(),"\t",temp4.strip(),"\t",temp5.strip(),"\t",temp1.strip(),"\t",temp2.strip())
    
    return 0

list_dir = os.listdir("Serotyping/")

for i in list_dir:
    inner_dir = os.listdir("Serotyping/" + i)
    for j in inner_dir:
        Fname = "Serotyping/" + i + "/" + j
        F1 = open(Fname,"r")
        pick_results(F1,j)
        F1.close()
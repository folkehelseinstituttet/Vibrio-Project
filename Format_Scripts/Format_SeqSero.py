import re
import sys
import os
from os import listdir

def pick_results(F,SID):
    for i in F:
        if re.search("Predicted antigenic profile",i):
            temp = i.split()[3]
            print (SID,"\t",temp)
    
    return 0

list_dir = os.listdir("Serotyping/")

for i in list_dir:
    inner_dir = os.listdir("Serotyping/" + i)
    for j in inner_dir:
        Fname = "Serotyping/" + i + "/" + j
        F1 = open(Fname,"r")
        pick_results(F1,j)
        F1.close()
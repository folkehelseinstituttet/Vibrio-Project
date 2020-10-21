import re
import os
import sys
#from prettytable import PrettyTable

def pick_results(F,SID):
    SID = SID.split(".")[0]
    for i in F:
        temp = i.split()
        if temp[3] == "S":
            species = temp[5] + "-" + temp[6]
            break 
    
    #print (temp[0],"\t",SID,"\t",species)
    txt = temp[0] + "," + SID + "," + species
    print txt
    
    return species

Kraken2_Reports = "Kraken2_Reports_2020/"

kraken2_files = os.listdir(Kraken2_Reports)

for i in kraken2_files:
    OF = Kraken2_Reports + "/" + i
    F1 = open(OF,"r")
    t = pick_results(F1,i)
    F1.close()

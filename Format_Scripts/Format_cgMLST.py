import re
import sys
import os
from os import listdir
from prettytable import PrettyTable

def pick_results(F,SID):
    N = 0
    for i in F:
        #print(i)
        if N == 1:
            temp = i.split()
            #t.add_row([SID,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7]])
            SID = SID.replace("_Trimmed","")
            print(SID,"\t",temp[0],"\t",temp[1],"\t",temp[2],"\t",temp[3],"\t",temp[4],"\t",temp[5],"\t",temp[6],"\t",temp[7])
        N += 1
    
    return 0



#t = PrettyTable(['Sample','ST','aroC','dnaN','hemD','hisD','purE','sucA','thrA'])


list_dir = os.listdir("cgMLST/")

for i in list_dir:
    inner_dir = os.listdir("cgMLST/" + i)
    Fname = "cgMLST/" + i + "/" + "mlst_report.tsv"
    F1 = open(Fname,"r")
    F = F1.readlines()
    t = pick_results(F,i)
    F1.close()

#print (t)
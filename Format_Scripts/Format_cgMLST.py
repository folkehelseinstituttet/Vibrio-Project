import re
import sys
import os
from os import listdir
from prettytable import PrettyTable

def pick_results(F,SID,t):
    N = 0
    for i in F:
        print(i)
        if N == 1:
            temp = i.split()
            t.add_row([SID,temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7]])
        N += 1
    
    return t

t = PrettyTable(['Sample','ST','aroC','dnaN','hemD','hisD','purE','sucA','thrA'])


list_dir = os.listdir("cgMLST/")

for i in list_dir:
    inner_dir = os.listdir("cgMLST/" + i)
    Fname = "cgMLST/" + i + "/" + "mlst_report.tsv"
    F1 = open(Fname,"r")
    F = F1.readlines()
    t = pick_results(F,i,t)
    F1.close()

print (t)
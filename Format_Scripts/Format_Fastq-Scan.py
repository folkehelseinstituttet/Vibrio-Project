import re
import sys
import os
from os import listdir

# os.system("conda activate Python3p7")

#from tabulate import tabulate
from prettytable import PrettyTable


def split_by_pattern(t):
    temp = t.split(":")[1]
    temp = temp.replace(",","")
    
    return temp

def pick_results(F,SID,t,b4c,status):
    for i in F:
        if re.search("read_total",i):
            reads = split_by_pattern(i)
            
        if re.search("coverage",i):
            coverage = split_by_pattern(i)

        if re.search("read_mean",i):
            read_mean = split_by_pattern(i)

        if re.search("read_std",i):
            read_SD = split_by_pattern(i)
    if status == "B4":
        b4c[SID] = reads
    else:
        prop = int(reads.strip())/int(b4c[SID])
        print(SID,"\t",reads.strip(),"\t",coverage.strip(),"\t",read_mean.strip(),"\t",read_SD.strip(),"\t",prop)    
        pass
    
    #print(SID,"\t",reads.strip(),"\t",coverage.strip(),"\t",read_mean.strip(),"\t",read_SD.strip(),"\t",prop)    
    t.add_row([SID,coverage,read_mean,read_SD])
    
    return b4c

list_dir = os.listdir("FastQ_Stats_Before_Cleaning_Dec2019/")

print ("FastQ_Stats_Before_Cleaning")
t = PrettyTable(['Sample', 'No. reads','Coverage','Read_SD'])
b4_clean = {}
for i in list_dir:
    Fname = "FastQ_Stats_Before_Cleaning_Dec2019/" + i
    F1 = open(Fname,"r")
    b4_clean = pick_results(F1,i,t,b4_clean,"B4")
    F1.close()

print("FastQ_Stats_After_Cleaning")

list_dir = os.listdir("FastQ_Stats_After_Cleaning_Dec2019/")

t = PrettyTable(['Sample', 'No. reads','Coverage','Read_SD'])
for i in list_dir:
    Fname = "FastQ_Stats_After_Cleaning_Dec2019/" + i
    F1 = open(Fname,"r")
    b4c = pick_results(F1,i,t,b4_clean,"AF")
    F1.close()

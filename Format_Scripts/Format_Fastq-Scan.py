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

def pick_results(F,SID,t):
    for i in F:
        if re.search("read_total",i):
            reads = split_by_pattern(i)
            
        if re.search("coverage",i):
            coverage = split_by_pattern(i)

        if re.search("read_mean",i):
            read_mean = split_by_pattern(i)
            #print (SID + "\tRead-Mean-" + result)

        if re.search("read_std",i):
            read_SD = split_by_pattern(i)
            #print (SID + "\tRead-SD-" + result)
    print(SID,"\t",coverage.strip(),"\t",read_mean.strip(),"\t",read_SD.strip())    
    t.add_row([SID,coverage,read_mean,read_SD])
    
    return t

list_dir = os.listdir("FastQ_Stats_Before_Cleaning/")

#print ("FastQ_Stats_Before_Cleaning")
t = PrettyTable(['Sample', 'No. reads','Coverage','Read_SD'])

for i in list_dir:
    Fname = "FastQ_Stats_Before_Cleaning/" + i
    F1 = open(Fname,"r")
    #t = pick_results(F1,i,t)
    F1.close()

#print(t)

list_dir = os.listdir("FastQ_Stats_After_Cleaning/")

#print ("FastQ_Stats_After_Cleaning")
t = PrettyTable(['Sample', 'No. reads','Coverage','Read_SD'])

for i in list_dir:
    Fname = "FastQ_Stats_After_Cleaning/" + i
    F1 = open(Fname,"r")
    t = pick_results(F1,i,t)
    F1.close()

#print(t)

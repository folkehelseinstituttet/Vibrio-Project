import re
import os
import sys
from prettytable import PrettyTable

AMR_Reports = "AMR/"

amr_files = os.listdir(AMR_Reports)

def format_the_data(F1):
    gene_drug = {}
    gene_mut = {}
    for i in F1:
        temp = i.split()
        gene_drug[temp[0]] = temp[2]
        gene_mut[temp[0]] = temp[1]
    
    return gene_drug,gene_mut

def pick_results(F,SID,t):
    SID = SID.split(".")[0]
    for i in F:
        temp = i.split()
        cluster = temp[6]
        mutation = temp[18]    
        t.add_row([SID,cluster,mutation])

    return t

F1 = open("AMR_Repertoire.tsv","r")
gene_drug, gene_mut = format_the_data(F1)
F1.close()

t = PrettyTable(['Sample', 'Cluster','Mutation'])

for i in amr_files:
    OF = AMR_Reports + i + "/" + "report.tsv"
    F1 = open(OF,"r")
    t = pick_results(F1,i,t)
    F1.close()
    
print(t)
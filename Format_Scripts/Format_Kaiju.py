import sys
import re
import os

def format_name(temp):
    tname = ""
    for j in range(3,len(temp)):
        tname = tname + "-" + temp[j]
    
    return tname

F1 = open("kaiju.names.out","r")

n_reads = 0
n_unclassified = 0
tax = {}
for i in F1:
    n_reads = n_reads + 1
    temp = i.split()
    #print (temp)
    # Unclassfied reads
    if temp[0] == 'U':
        n_unclassified = n_unclassified + 1
    else:
        tax_name = format_name(temp)
        if tax_name in tax:
            tax[tax_name] += 1
        else:
            tax[tax_name] = 1

F1.close()

print ("Total No. of Reads:",n_reads)
print ("No. of Unclassified:",n_unclassified,"\t",(n_unclassified/n_reads)*100)
B = 0
for i in tax:
    tax[i] = (tax[i]/n_reads)*100
    B += tax[i]
    print (i,"\t",tax[i])


print (B)
# -max_target_seqs 1
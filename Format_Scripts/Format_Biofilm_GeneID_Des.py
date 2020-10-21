import sys
import re

f1 = open("Biofilm_GeneID_Des.csv","r")
d = f1.readlines()

for i in range(len(d)):
    if re.search("^>",d[i]):
        temp = d[i].split()[0]
        temp = temp.replace(">","")
        des = d[i-1]
        print (temp,"\t",des.strip())
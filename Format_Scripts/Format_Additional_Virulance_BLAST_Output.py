import sys
import os
import re
from os import listdir


# Sub programs

def gene_size(grange):
    temp = grange.split(":")
    gname = temp[0]
    gene_range = temp[1].split("-")
    gene_range[0] = gene_range[0].replace("c","")
    gsize = int(gene_range[1]) - int(gene_range[0])
    
    return gsize
    
def format_filter(f,l):
    fname = l + f
    F1 = open(fname,"r")
    for i in F1:
        temp = i.split()
        gsize = gene_size(temp[1])
        gene_prop = (float(temp[3])/gsize)*100
        if float(temp[2]) >= identity and gene_prop >= gene_length:
            #print (f,",",i.strip(),",",GID_Des[temp[1]].strip())
            print (f,",",temp[0],",",temp[1],",",temp[2],",",temp[3])

    F1.close()

    return 0

######################################################################
###################### Main Script ###################################
######################################################################
file_location = "/cluster/home/jeevka/2019_Oct_Vibrio/Virulance_Addtional_Out/"

identity = 80
gene_length = 80

blast_output_files = [f for f in listdir(file_location)]

# Making Biofilm GeneID anmd description

"""
GID_Des = {}
F2 = open("Biofilms_Formatted_GeneID_Des.csv","r")
for i in F2:
    temp = i.split("\t")    
    GID_Des[temp[0].strip()] = temp[1]

F2.close()
"""

for i in blast_output_files:
    format_filter(i,file_location)

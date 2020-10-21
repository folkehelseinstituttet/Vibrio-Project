import sys
import re


Fname = "/cluster/projects/nn9680k/DBs/Vibrio_Biofilm_Genes/Vibrio_Biofilm_Genes_271019.fasta"

F1 = open(Fname,"r")

for i in F1:
    if re.search(">",i):
        temp = i.split()
        temp1 = temp[0].split(":")
        
        seq_id = temp[0].replace(">","")
        gene_range = temp1[1].split("-")
        GR1 = gene_range[0];GR2 = gene_range[1]
        GR1 = GR1.replace("c","")
        gene_length = abs(int(GR2) - int(GR1))
        #sprint (seq_id,GR1,GR2,gene_length)
        print seq_id,"\t","1","\t",gene_length

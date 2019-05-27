import re
import os
import sys
from prettytable import PrettyTable

#############################################################################
####################    Subprograms start here  #############################
#############################################################################   
"""
store the Mut-drug data in dictionary 
"""
def format_the_data_1(F1):
    gene_drug = {}
    gene_mut = {}
    for i in F1:
        temp = i.split()
        gene_drug[temp[0]] = temp[2]
        gene_mut[temp[0]] = temp[1]
    
    return gene_drug,gene_mut

def format_the_data_2(F1):
    gene_drug = {}
    for i in F1:
        temp = i.split()
        gene_drug[temp[0]] = temp[1]
    
    return gene_drug

"""
Compares gene, mutations and predicts the drug resistances
"""
def mutation_AMR_1(dat,gene_drug,gene_mut,SID):
    temp = dat.split()
    for i in gene_mut:
        """
        check for gene name
        """
        if re.search(i,temp[6]):
            """
            check for mutation
            """
            if re.search(gene_mut[i],temp[16]):
                print (SID,"\t",i,"\t",gene_mut[i],"\t",gene_drug[i])
    
    return 0


"""
Compares gene and predicts the drug resistances
"""
def mutation_AMR_2(dat,gene_drug,SID):
    temp = dat.split()
    for i in gene_drug:
        """
        check for gene name
        """
        if re.search(i,temp[6]):
            """
            check for mutation
            """
            if re.search(gene_drug[i],temp[16]):
                print (SID,"\t",i,"\t",gene_drug[i])
    
    return 0

"""
Filter the data based on the conditions
"""
def filter_results(F,SID,t,gene_drug,gene_mut,gene_drug_wo_mut):
    SID = SID.split(".")[0]
    for i in range(1,len(F)):
        temp = F[i].split()
        
        """
        Calculating the mapping coverage
        """
        map_cov = 100 * (float(temp[8])/float(temp[7]))
        
        """
        if the value is dot(.) in the data, then it will end up in error
        """
        if temp[13] == ".":
            temp[13] = 0
        
        if temp[26] == ".":
            temp[26] = 0
                    
        n_read_map = 0
        species_id = 0        
        
        """
        Some data points are just dot(.) So, we need try and except
        """
        try:
            T = temp[26].split(";")
            if 'ND' in T:
                T = T.replace('ND',0)
        except:
            T = 0
        
        if isinstance(T,list):
            if len(T) > 1:
                #print ("*****",T)
                if int(T[0]) >= 25:
                    n_read_map = 1
                else:
                    if int(T[0]) >= 25 and int(T[1]) >= 25 and int(T[2]) >= 25:
                        n_read_map = 1
        
        """
        Check if this is Salmonella
        """
        if re.search("Salmonella",F[i]):
            species_id = 1
        
        """
        Filtering conditions:
            identity >=97% and map_coverage >=95% and read_mapping >=25 and species must be "salmonella"
        """
        if float(temp[9]) >= 97 and map_cov >= 95 and float(temp[13]) == 1 and n_read_map == 1 and species_id == 1:
            """
            if the data passes the condition check for gene and mutation to predict Drug resistanec
            """
            mutation_AMR_1(F[i].strip(),gene_drug,gene_mut,SID)

            """
            if the data passes the condition check for gene/allele to predict Drug resistanec
            """
            mutation_AMR_2(F[i].strip(),gene_drug_wo_mut,SID)
            
    return 0

#############################################################################
####################    Main script starts here  ############################
#############################################################################

AMR_Reports = "AMR/"

amr_files = os.listdir(AMR_Reports)

"""
Reading the gene,mutation and drug files
"""
F1 = open("AMR_Repertoire.tsv","r")
gene_drug, gene_mut = format_the_data_1(F1)
F1.close()


"""
Reading the gene and drug files
"""
F1 = open("AMR_Repertoire_wo_mut.tsv","r")
gene_drug_wo_mut = format_the_data_2(F1)
F1.close()

t = PrettyTable(['Sample', 'Cluster','Mutation'])

for i in amr_files:
    OF = AMR_Reports + i + "/" + "report.tsv"
    F1 = open(OF,"r")
    #print (i)
    """
    # Filter 1: based on
        identity >= 97%
        Mapping coverage >= 95%
        know_var == 1
        Free text ~= salmonella
        read coverage
    """
    dat = F1.readlines()
    filter_results(dat,i,t,gene_drug,gene_mut,gene_drug_wo_mut)
    F1.close()
    
#print(t)
import sys
import re
import os


"""
Sub programs
"""

def print_column_title(f,sample_ID,DB):
    F1 = open(f,"r")
    F2 = F1.readlines()
    title = "Sample_ID" + "," + "DB" + ","
    T = F2[0].split()
    for i in T:
        title = title + "," + i
    print title
    
    return 0

def format_file(f,SID,DB,sp):
    F1 = open(f,"r")
    N = 0
    for i in F1:
        if not re.search("^#",i):
            try:
                temp = i.split()    
                T = SID + "," + sp[SID].strip()  + "," + DB
                for j in range(30):
                    T = T + "," + temp[j]
                
                free_text = ""
                for j in range(30,len(temp)):
                    free_text = free_text + " " + temp[j]
                
                #print T + "," + sp[SID].strip() + "," + free_text
                print T + "," + free_text
            except:
                pass
            
    return 0

"""
Main script
"""

species = {}
KF = open("/cluster/projects/nn9680k/Vibrio_Project/Kraken2_Results_Dec2019.csv","r")
for i in KF:
    temp = i.split(",")
    species[temp[1]] = temp[2]

KF.close()

input_files = "/cluster/projects/nn9680k/Vibrio_Project/Ref_Mapping_AMR/"
input_files = "/cluster/projects/nn9680k/Vibrio_Project/Ref_Mapping_AMR/AMR_Daniel_Genes/"
input_files = "/cluster/projects/nn9680k/Vibrio_Project/Biofilm_Fastq_May2020/"
input_files = "/cluster/projects/nn9680k/Vibrio_Project/Ref_Mapping_AMR_May2020/"
List_folders = os.listdir(input_files)
title = "SampleID,DB,#ariba_ref_name,ref_name,gene,var_only,flag,reads,cluster,ref_len,ref_base_assembled,pc_ident,ctg,ctg_len,ctg_cov,known_var,var_type,var_seq_type,known_var_change,has_known_var,ref_ctg_change,ref_ctg_effect,ref_start,ref_end,ref_nt,ctg_start,ctg_end,ctg_nt,smtls_total_depth,smtls_ntssmtls_nts_depth,var_description,free_text"
print title
for i in List_folders:
    if not i == "Ref_Map.sh":
        report_file = input_files + i + "/report.tsv"
        try:
            F1 = open(report_file,"r")
            T = i.split(".")
            sample_ID = T[0]
            DB = T[2] #+ "_Daniel_Genes"
            #print_column_title(report_file,sample_ID,DB)
            format_file(report_file,sample_ID,DB,species)    
        except:
            print sample_ID,",NO_Results"
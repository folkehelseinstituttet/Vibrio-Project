import sys
import re

########################################
########## Sub-Programs ################
########################################
def open_file(fname):
    F = open(fname,"r")
    return F 


def format_1(fastq):
    dat = {}
    for i in fastq:
        temp = i.split()
        temp[0] = temp[0].replace("_Trimmed","")
        dat[temp[0]] = temp[1] + "-" + temp[2] + "-" + temp[3].strip()
    
    return dat

def format_2(kmerID):
    dat = {}
    for i in kmerID:
        temp = i.split()
        dat[temp[0]] = temp[1] + "-" + temp[2]
    
    return dat

def format_3(cgMLST):
    dat = {}
    for i in kmerID:
        temp = i.split()
        temp[0] = temp[0].replace("_Trimmed","")
        dat[temp[0]] = temp[1] + "-" + temp[2] + "-" + temp[3] + "-" + temp[4] + "-" + temp[5] + "-" + temp[6] + "-" + temp[7] + "-" + temp[8]
    
    return dat

def format_4(asm_stat):
    dat = {}
    for i in asm_stat:
        temp = i.split()
        temp[0] = temp[0].replace("_Trimmed","")
        dat[temp[0]] = temp[1] + "-" + temp[2] + "-" + temp[3] + "-" + temp[4]
    
    return dat

def format_5(seq_sero):
    dat = {}
    for i in seq_sero:
        temp = i.split()
        temp[0] = temp[0].replace("_Trimmed_1.txt","")
        temp[0] = temp[0].replace("_Trimmed_2.txt","")
        dat[temp[0]] = temp[1] + "#" + temp[2] + "#" + temp[3] + "#" + temp[4] + "#" + temp[5]
    
    return dat


def format_6(amr_report):
    dat = {}
    for i in amr_report:
        temp = i.split()
        temp[0] = temp[0].replace("_Trimmed","")
        dat[temp[0]] = temp[1] + "-" + temp[2] + "-" + temp[3] 
    
    return dat

def format_7(kraken_report):
    dat = {}
    for i in kraken_report:
        temp = i.split()
        temp[1] = temp[1].replace("_Trimmed","")
        dat[temp[1]] = temp[0] + "#" + temp[2] 
    
    return dat
########################################
########## Main Programs ###############
########################################

fastq = open_file("FastQ-Stat_Summary.tsv")
f_stat = format_1(fastq)

kmerID = open_file("Summarize_KmerID.tsv")
kmerID_stat = format_2(kmerID)

cgMLST = open_file("cgMLST.tsv")
cgMLST_stat = format_3(cgMLST)

asm_stat = open_file("Assembly_Stat_Summary.tsv")
asm_stat = format_4(asm_stat)

seq_sero = open_file("SeqSero_Summary.tsv")
seq_sero = format_5(seq_sero)

amr_report = open_file("AMR_Summary_Report.tsv")
amr_report = format_6(amr_report)

kraken2_report = open_file("Kraken2_Summary_Report.tsv")
kraken2_report = format_7(kraken2_report)

print ("Sample_ID#N_Reads(M)#Coverage#Species-KmerID#KmerID_Coverage#Species-kraken2#Coverage#SeqSero_O-antigen#SeqSero_H1-antigen#SeqSero_H2-antigen#SeqSero_AntigenicProfile#SeqSero_Serotype#\
       MLST_ST#MLST_aroc#MLST_dnaN#MLST_hemD#MLST_hisD#MLSTpurE#MLST_sucA#MLST_thrA")

for i in f_stat:
    # FastQ Stat
    temp1 = f_stat[i].split("-")
    
    # KmerID
    temp2 = kmerID_stat[i].split("-")
    
    # Kraken2
    temp3 = kraken2_report[i].split("#")
    
    # SeqSero
    temp4 = seq_sero[i].split("#")
    
    # Assembly Stat
    temp5 = asm_stat.split()
    
    # AMR Report
    temp6 = amr_report.split()
    
    # Main output
    txt = i.split("_")[0] + "#" + temp1[0] + "#" + temp1[1] + "#" + temp2[1] + "#" + temp2[0] + "#" + temp3[1] + "#" + temp3[0] + "#" + temp4[1] + "#" + temp4[2] + "#" + temp4[3] + "#" + temp4[4]
    
    print (txt)
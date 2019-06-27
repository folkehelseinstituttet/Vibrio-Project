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
        dat[temp[0]] = temp[1] + "-" + temp[2] + "-" + temp[3] + "-" + temp[4] + "-" + temp[5].strip()
    
    return dat

def format_2(kmerID):
    dat = {}
    for i in kmerID:
        temp = i.split()
        dat[temp[0]] = temp[1] + "-" + temp[2]
    
    return dat

def format_3(cgMLST):
    dat = {}
    for i in cgMLST:
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
        dat[temp[0]] = temp[1] + "#" + temp[2] + "#" + temp[3] + "#" + temp[4] + "#" + temp[5] + "#" + temp[6]
    
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
cgMLST_summary = format_3(cgMLST)

asm_stat = open_file("Assembly_Stat_Summary.tsv")
asm_stat = format_4(asm_stat)

seq_sero = open_file("SeqSero_Summary.tsv")
seq_sero = format_5(seq_sero)

amr_report = open_file("AMR_Summary_Report.tsv")
amr_report = format_6(amr_report)

# Make the head6 from mut list Initialize the mutations
AMR_Mut = {}
head6 = ""
AMR_File = open("AMR_Mut_List.csv","r")
for i in AMR_File:
    AMR_Mut[i.strip()] = "X"
    head6 = head6 + "#" + i.strip()

kraken2_report = open_file("Kraken2_Summary_Report.tsv")
kraken2_report = format_7(kraken2_report)

head1 = "Sample_ID#N_Reads(M)#Avg-read-Size#Pro. reads passed#AsmSize#N_Scaf#Avg-Scaf-size#N50#Coverage#KmerContent"
head2 = "#Species-KmerID#KmerID_Coverage#Species-kraken2#Coverage"
head3 = "#SeqSero_AntiGenProfile#SeqSero_H1-antigen#SeqSero_H2-antigen#SeqSero_AntigenicProfile#SeqSero_Serotype"
head4 = "#MLST_ST#MLST_aroc#MLST_dnaN#MLST_hemD#MLST_hisD#MLSTpurE#MLST_sucA#MLST_thrA"
head5 = "#AMR_AG#AMR_BL#AMR_Col#AMR_FQ#AMR_FOS#AMR_MLS#AMR_PHE#AMR_SUL#AMR_TET#AMR_TriMET"

print (head1 + head2 + head3 + head4 + head5 + head6)

for i in f_stat:
    
    sample_id = i.split("_")[0]
    
    # FastQ Stat
    (n_reads,fq_cov,fq_mean,fq_sd,fq_pro) = f_stat[i].split("-")
    
    # KmerID
    (kmer_per,kmer_species) = kmerID_stat[i].split("-")
    
    # Kraken2
    (kraken_cov,kraken_species) = kraken2_report[i].split("#")
    
    # Serotyping - SeqSero
    (O_antigen,H2_antigen,H1_antigen,dummy_var,SeqSero_AntigenicProfile,SeqSero_Serotype) = seq_sero[i].split("#")
    
    # cgMLST
    (ST,aroc,dnaN,hemD,hisD,purE,sucA,thrA) = cgMLST_summary[i].split("-")

    # Assembly Stat
    try:
        (asm_size,n_contig,avg_size,N50) = asm_stat[i].split("-")
    except:
        (asm_size,n_contig,avg_size,N50) = ("X","X","X","X")
    
    # AMR Report
    try:
        temp6 = amr_report[i].split()
    except:
        temp6 = ["XX-XX-XX"]
        
    
    # Main output
    
    # FastQ and Assembly
    txt1 = sample_id + "#" + n_reads + "#" + fq_mean + "#" + fq_pro  + "#" + asm_size + "#" + n_contig + "#" + avg_size + "#" + N50 + "#"
    
    # Species identification
    txt2 = kmer_species + "#" + kmer_per + "#" + kraken_species + "#" + kraken_cov + "#"
    
    # Serotyping
    txt3 = O_antigen + "#" + H2_antigen + "#" + H1_antigen + "#" + dummy_var + "#" + SeqSero_AntigenicProfile + "#" + SeqSero_Serotype + "#"

    # cgMLST
    txt4 = ST + "#" + aroc + "#" + dnaN + "#" + hemD + "#" + hisD + "#" + purE + "#" + sucA + "#" + thrA + "#"
    
    # AMR
    txt5 = ""

    
    print (txt1 + txt2 + txt3 + txt4)
    #sys.exit()
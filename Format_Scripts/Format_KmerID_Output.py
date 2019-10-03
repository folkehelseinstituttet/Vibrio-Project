import os
import re
import Sub_Functions as SF

OPL = "KmerID_Reports/"
#OPL = "Test_KmerID_Output/"

OP_files = SF.list_paird_end_files(OPL)

for i in OP_files:
    sample_id = i.split("_Trimmed")[0]
    F1 = open(OPL + i,"r")
    D = F1.readlines()
    #D = [line.rstrip('\n') for line in open(OPL + i)]
    print(sample_id,"\t",D[2].strip())
    
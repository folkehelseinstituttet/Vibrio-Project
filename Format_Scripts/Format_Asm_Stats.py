import re
import os
import sys
#from prettytable import PrettyTable

assembly_statistics = "Denova_Assemblies/Assembly_Statistics/"

stat_files = os.listdir(assembly_statistics)

def pick_results(F,SID):
    SID = SID.split(".")[0]
    for i in F:
        if re.search("sum",i):
            temp = i.split()
            GSize = temp[2]
            GSize = GSize.replace(",","")
            N_scaf = temp[5]
            N_scaf = N_scaf.replace(",","")
            Avg_size = temp[8]
            Avg_size = Avg_size.replace(",","")
        if re.search("N50",i):
            temp = i.split()
            N50 = temp[2]
            N50 = N50.replace(",","")
    print (SID,"\t",GSize,"\t",N_scaf,"\t",Avg_size,"\t",N50)

    return 0

for i in stat_files:
    #stat_file = assembly_statistics + i
    OF = assembly_statistics + i
    F1 = open(OF,"r")
    t = pick_results(F1,i)
    F1.close()
from os import listdir
import sys
import os
import re

file_location = "/cluster/home/jeevka/2019_Oct_Vibrio/Vibrio_Data_All/"
#file_location = "/cluster/home/jeevka/2019_Oct_Vibrio/Trimmed_Fastq_Files/"

fastq_files_list = [f for f in listdir(file_location)]

for i in fastq_files_list:
    f = file_location + i
    f_size = os.path.getsize(f)/(1024*1024)
    f_size = float("{0:.2f}".format(f_size))
    if re.search("^NO_",i):
        print (i,"\t",f_size,"\t","Norway")
    elif re.search("^Se_",i):
        print (i,"\t",f_size,"\t","Sweden")
    elif re.search("^DK_",i):
        print (i,"\t",f_size,"\t","Denmark")
    elif re.search("^Fi_",i):
        print (i,"\t",f_size,"\t","Finland")
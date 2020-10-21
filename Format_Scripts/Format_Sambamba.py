import re
import sys

Fname = sys.argv[1]

F1 = open(Fname,"r")

# Gene Descriptions
F2 = open("Biofilms_Formatted_GeneID_Des.csv","r")
GID_Des = {}
for i in F2:
    temp = i.split("\t")
    GID_Des[temp[0].strip()] = temp[1]

F2.close()

sample_id = Fname.split("/")[1]
sample_id = sample_id.split(".")[0]
for i in F1:
    if not re.search("^#",i):
        temp1 = i.split()
        if int(temp1[3]) != 0:
            print (sample_id,",",GID_Des[temp1[0]].strip(),",",temp1[0],",",temp1[3],",",temp1[4])
        
F1.close()

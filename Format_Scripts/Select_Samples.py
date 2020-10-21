import sys
import re

# To be selected  Sample List 
F1 = open("Sample_List.csv","r")

# Whole Result List
F2 =  open("/cluster/projects/nn9680k/Vibrio_Project/AMR_May2020.csv","r")

samples = {}

# Store the to be selected sample IDs
for i in F1:
    id = i.strip()
    samples[id] = id

F1.close()

for j in F2:
    temp = j.split(",")
    if samples.has_key(temp[0]):
        print j.strip()

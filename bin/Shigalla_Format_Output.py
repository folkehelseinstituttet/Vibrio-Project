import re
import sys
import os

file_location = sys.argv[1]

list_of_files = os.listdir(file_location)

for i in list_of_files:
    fname = file_location + i
    F1 = open(fname,"r")
    for j in F1:
        if not re.search("^sample",j):
            print (j.strip())
    F1.close()

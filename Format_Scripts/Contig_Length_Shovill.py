import sys
import re

F1 = open("Se_9-18.csv","r")
N1 = 0
N2 = 0
for i in F1:
	temp = i.split()
	L = int(temp[1].split("=")[1])
	if L < 500: 
		N1 = N1 + 1
	if L < 1000:
		N2 = N2 + 1
	#print temp[0],"\t",temp[1]


print "Less than 500:",N1
print "Less than 1000:",N2

	


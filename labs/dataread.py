import csv 

FILENAME= "data.csv" 
DATADIR = "C:/Users/jmnic/Desktop/ATU Galway-Mayo/WSAA/labs/" 
with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
for line in reader:         
    print (line)
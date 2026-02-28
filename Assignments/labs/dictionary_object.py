# The CVS file  have been read in as adistionary object

import csv
FILENAME = "data.csv"
DATADIR = "C:/Users/jmnic/Desktop/ATU Galway-Mayo/WSAA/labs/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC) 
    total = 0 
    count = 0 
    for line in reader: 
        total += line['age'] 
        # print (line) 
        count +=1 
    print (f"average is {total/(count)}") # why is there no -1 this time? 
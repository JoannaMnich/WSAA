#  calculate the average age
#  Convert the string that is read into an integer

import csv

FILENAME = "data.csv"
DATADIR = "C:/Users/jmnic/Desktop/ATU Galway-Mayo/WSAA/labs/"

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    linecount = 0 
    total = 0 
    for line in reader: 
        if not linecount: # first row ie header row 
            pass
        else: # all subsequent rows 
            total += int(line[1]) # why 1 
        linecount += 1 
    print (f"average is {total/(linecount-1)}") # why -1 ? 

# Use the quote parameter to read in the numbers as floats 

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) 
    linecount = 0 
    total = 0 
    for line in reader: 
        if not linecount: # first row ie header row 
            pass 
        else: # all subsequent rows 
            total += line[1] # why 1 
 
        linecount += 1 
    print (f"average is {total/(linecount-1)}") # why -1 ? 
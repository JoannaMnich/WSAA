import csv 

FILENAME = "data.csv"
DATADIR = "C:/Users/jmnic/Desktop/ATU Galway-Mayo/WSAA/labs/"

with open(DATADIR + FILENAME, "rt", newline="") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)

# there is code not shown here 
with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    linecount = 0 
    for line in reader: 
        if not linecount: # first row ie header row 
            print (f"{line}\n-------------------") 
        else: # all subsequent rows 
            print (line) 
        linecount += 1 

with open(DATADIR + FILENAME, "rt", newline="") as fp:
    reader = csv.reader(fp, delimiter=",")

    header = next(reader)          # read header line
    print("Header:")
    print(header)
    print("-------------------")

    for line in reader:            # remaining data rows
        print(line)

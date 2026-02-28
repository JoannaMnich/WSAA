import requests 
import csv  

from xml.dom.minidom import parseString 
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML" 
page = requests.get(url) 
doc = parseString(page.content) 

# check it works 
print (doc.toprettyxml()) #output to console comment this out once you know it works 

# if I want to store the xml in a file. You can comment this out later 
with open("trainxml.xml","w") as xmlfp: 
    doc.writexml(xmlfp)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") 
for objTrainPositionsNode in objTrainPositionsNodes: 
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0) 
    traincode = traincodenode.firstChild.nodeValue.strip() 
    print (traincode) 

import csv

# write the file without blank lines
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()

        # write each train code as a row
        train_writer.writerow([traincode])

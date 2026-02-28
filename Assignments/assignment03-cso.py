# Retrieves the dataset for the "exchequer account (historical series) and save in cso.json file
# Author: Joanna Mnich

import requests
import json
url="https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
 
response = requests.get(url)

if response.status_code == 200:
    with open("cso.json", "w") as f:
        f.write(response.text)
    print("Dataset saved to cso.json")
else:
    print("Failed to retrieve data")

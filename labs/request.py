from urllib import response
from httpcore import URL
import requests 
#url = "http://google.com" 
#response = requests.get(url) 
#print (response.text) 


#URL = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(URL) 
#print (response.json()) 


URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching books:", response.status_code)
        return None

if __name__ == "__main__":
    books = readbooks()
    print(books)


import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"


# ---------- READ ALL ----------
def readbooks():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching books:", response.status_code)
        return None


# ---------- READ BY ID ----------
def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching book:", response.status_code)
        return None


# ---------- CREATE ----------
def createbook(book):
    response = requests.post(URL, json=book)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error creating book:", response.status_code)
        return None


# ---------- UPDATE ----------
def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error updating book:", response.status_code)
        return None


# ---------- DELETE ----------
def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error deleting book:", response.status_code)
        return None


# ---------- TESTING CODE ----------
if __name__ == "__main__":

    print("Creating book...")
    newbook = {
        "title": "Test Python Book",
        "author": "JM",
        "price": 1234
    }

    created = createbook(newbook)
    print("Created:", created)

    book_id = created["id"]

    print("\nReading book by ID...")
    print(readbook(book_id))

    print("\nUpdating book price...")
    update = updatebook(book_id, {"price": 2000})
    print(update)

    print("\nReading updated book...")
    print(readbook(book_id))

    print("\nDeleting book...")
    print(deletebook(book_id))

    print("\nTrying to read deleted book...")
    print(readbook(book_id))




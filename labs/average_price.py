import requests
from xlwings import books

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def get_average_price():
    response = requests.get(URL)

    if response.status_code != 200:
        print("Error fetching books:", response.status_code)
        return

    books = response.json()

    total = 0
    count = 0

    for book in books:
        price = book.get("price")

        if price is not None:
            total += price
            count += 1

    if count == 0:
        print("No valid book prices found.")
        return

    average = total / count
    print("Average book price:", average)


if __name__ == "__main__":
    get_average_price()




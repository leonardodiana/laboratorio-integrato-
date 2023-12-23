import requests

def updateItem():
    r=requests.get("http://127.0.0.1:5000/items")
    x=requests.post("http://127.0.0.1:8000/items", r)

def main():
    updateItem()

main()
import requests
from bs4 import BeautifulSoup

url = input("Enter full URL: ")
file = input("Enter destination text (txt) file name: ") + ".txt"
r = requests.get(url)

f = open(file, "w")
f.write("{}".format(r.text))
f.close()

print("HTML scraped and written in {} file".format(file))

from bs4 import BeautifulSoup
import requests

r=requests.get("https://www.iiit.ac.in/people/faculty/")

soup = BeautifulSoup(r.text)

# textLink=r.data
for name in soup.find_all('h3', class_ = "name"):
    print(name.a.text)

import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

def fetch(l):
    response = requests.get(l)
    return response.text

def clean(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup.select("span.titleline > a")  # titles ONLY

print("Starting..")

html = fetch(url)
headings = clean(html)

file = "NewsTable.csv"
with open(file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])

    for tag in headings:
        title = tag.get_text(strip=True)
        link = tag.get("href")
        writer.writerow([title, link])

print("Finished.")

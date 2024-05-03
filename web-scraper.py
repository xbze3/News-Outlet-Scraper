import requests
import re
from bs4 import BeautifulSoup
import pyfiglet
import datetime

ascii_banner = pyfiglet.figlet_format("NEWS SCRAPER")

print(" " + "=" * 78)
print(ascii_banner)
print(" " + "=" * 78)
print(" News Scraper")
print(" by @xbxe3 on GitHub")
print(" " + "=" * 78)
search = input(" Search Term(s): ")
print(" Date / Time: " + str(datetime.datetime.now()))
print(" " + "=" * 78)

def getBloomberg(userInput):

    userInput = userInput.replace(" ", "%20")
    headers = {'User-Agent': 'Mozilla/5.0'}

    URL = f"https://www.bloomberg.com/search?query={userInput}"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    eyebrowData = [x.get_text() for x in soup.find_all('div', attrs={'class': lambda x: x and re.compile(r'^eyebrow').match(x)})]
    headlineData = [x.get_text() for x in soup.find_all('a', attrs={'class': lambda x: x and re.compile(r'^headline').match(x)})]
    link = [a['href'] for a in soup.find_all('a', class_= lambda x: x and re.compile(r'^headline').match(x), href=True) if a.text]
    publishDate = [x.get_text() for x in soup.find_all('div', attrs={'class': lambda x: x and re.compile(r'^publishedAt').match(x)})]

    for i in range(0, len(eyebrowData)):
        print(f"\n [Sector]: {eyebrowData[i].upper()}\n [Headline]: {headlineData[i]}\n [Publish On]: {publishDate[i]}\n [Link]: {link[i]}")

    print("\n " + "=" * 36 + " Done " + "=" * 36)

getBloomberg(search)

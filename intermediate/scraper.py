 # From archive, follow each link, find the  image in that linked page, and download image

 # Concepts
 # 1. Downloading things => urllib
 # 2. Parsing stuff out of HTML => BeautifulSoup

import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Download the index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()

# For each link on the index page:
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following link:", link)
    href = urljoin(base_url, link["href"])
# Follow the link and pull down the image on that linked page
 # From archive, follow each link, find the  image in that linked page, and download image

 # Concepts
 # 1. Downloading things => urllib
 # 2. Parsing stuff out of HTML => BeautifulSoup

import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

# Download the index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()
download_directory = "apod_pictures"

# For each link on the index page:
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following link:", link)
    href = urljoin(base_url, link["href"])
    # Follow the link and pull down the image on that linked page
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href  =urljoin(href, img["src"])
        print("Downloading image:", img_href)
        img_name = img_href.split('/')[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
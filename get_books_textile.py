#!/usr/bin/env python

# Get all books from [http://privateweb.iitd.ac.in/~tt1140868/summerbooks/]
import os
import requests
from bs4 import BeautifulSoup as bs
from urlparse import urljoin
from subprocess import check_call

url = "http://privateweb.iitd.ac.in/~tt1140868/summerbooks/"
r = requests.get(url) # may need to unset proxy
soup = bs(r.text, "html.parser")

bdiv = soup.find("div", {"class":"allbookscontainer"})
categories = bdiv.find_all("div",{'class':'row booksholder'}) # class=booksholder will also work

def get_category_data (cat):
	cat_name = cat.find("div", {'class':'bookcategory'}).get_text().strip()
	a_tags = cat.find_all('a')
	links_and_images = [(urljoin(url,a.get('href')),urljoin(url,a.img.get('src'))) for a in a_tags]
	return (cat_name, links_and_images)

dl_data = [get_category_data(cat) for cat in categories]

for (cat,links_and_images) in dl_data:
	print "Downloading {cat} ...".format(cat=cat)
	
	#create directory for category
	if not os.path.exists(cat):
		os.makedirs(cat)

	for (link,img) in links_and_images:
		# using `wget -P` (see [http://stackoverflow.com/questions/1078524/how-to-specify-the-location-with-wget])
		check_call(['wget','-P',cat,img,link])

	print "[Done] {cat}".format(cat=cat)

#!usr/bin/python

import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)  # instore the information
	html = page.read()   #read the page
	return html

def getImg(html):
	reg = r'src="(.*?\.jpg)" arg'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl, '%s.jpg' %x)
		x+=1

html = getHtml("http://tulane.edu")
print getImg(html)


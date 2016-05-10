#usr/bin/python


import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImage(html):
	reg = r'src="(.*?\.jpg)" '
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0

	for imgurl in imglist:
		urllib.urlretrieve(imgurl, '%s.jpg' % x)
		x += 1
html = getHtml("http://www.rev.state.la.us/")	
# import urllib2




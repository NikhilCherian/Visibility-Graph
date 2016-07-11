import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/india/historic-inflation/cpi-inflation-india.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\htmldoc.html"
file=open(filename,'wb')
print >>file, html
file.close()

import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/israel/historic-inflation/cpi-inflation-israel.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\Inflationdata_Israel\htmldoc_Inflation_Israel.html"
file=open(filename,'wb')
print >>file, html
file.close()

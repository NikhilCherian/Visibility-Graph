import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/south-korea/historic-inflation/cpi-inflation-south-korea.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\Inflationdata_SouthKorea\htmldoc_Inflation_SouthKorea.html"
file=open(filename,'wb')
print >>file, html
file.close()

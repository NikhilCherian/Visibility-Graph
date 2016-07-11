import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/luxembourg/historic-inflation/cpi-inflation-luxembourg.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\Inflationdata_Luxembourg\htmldoc_Inflation_Luxembourg.html"
file=open(filename,'wb')
print >>file, html
file.close()

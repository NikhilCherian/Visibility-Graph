import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/great-britain/historic-inflation/cpi-inflation-great-britain.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\Inflationdata_GreatBritain\htmldoc_Inflation_GreatBritain.html"
file=open(filename,'wb')
print >>file, html
file.close()

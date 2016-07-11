import urllib2
from bs4 import BeautifulSoup


url= 'http://www.inflation.eu/inflation-rates/united-states/historic-inflation/cpi-inflation-united-states.aspx'
res= urllib2.urlopen(url)
html= res.read()

filename= "F:\git\Inflation_Countries_Data\Inflationdata_UnitedStates\htmldoc_Inflation_UnitedStates.html"
file=open(filename,'wb')
print >>file, html
file.close()

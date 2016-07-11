#BeautifulSoup.prettify(html)
import urllib2
import re
import csv
from bs4 import BeautifulSoup

favg=open('F:\git\Inflation_Countries_Data\Inflationdata_Luxembourg\Averageinflation_Luxembourg.csv','wb')
fannu=open('F:\git\Inflation_Countries_Data\Inflationdata_Luxembourg\Annualinflation_Luxembourg.csv','wb')



fl=open("F:\git\Inflation_Countries_Data\Inflationdata_Luxembourg\htmldoc_Inflation_Luxembourg.html",'r')

soup = BeautifulSoup(fl,'html.parser')
#print soup.prettify()[0:1000]

print soup.title

#soup.table['class']

#print (soup.findAll('class'))
tablestats = soup.find('table',{'class': 'maintable'})


#print tablestats

litavg=[]
lit2=[]
litnor=[]
for row in tablestats.findAll('tr',{'class': 'tabledata1'}):
    column= row.findAll("td")
    x= column[0].find('a',class_=True)['title']
    print x
    if re.search("Average CPI inflation",x):
        print "Average"
        year1=column[0].getText()
        y1=re.sub('\CPI Luxembourg', '', year1)
        CPI= column[1].getText()
        c1=re.sub('\%', '', CPI)
        print y1,c1
        try :
            litavg.append([int(y1),float(c1)])
        except ValueError,e :
            continue

        year2=column[3].getText()
        y2=re.sub('\CPI Luxembourg', '', year2)
        CPI2=column[4].getText()
        c2=re.sub('\%', '', CPI2)
        print y2, c2
        try :
            litavg.append([int(y2),float(c2)])
        except ValueError,e :
            continue

    else:
        print "Not Average"
        year1=column[0].getText()
        y1=re.sub('\CPI Luxembourg', '', year1)
        CPI= column[1].getText()
        c1=re.sub('\%', '', CPI)
        print y1,c1
        try :
            litnor.append([int(y1),float(c1)])
        except ValueError,e :
            continue

        year2=column[3].getText()
        y2=re.sub('\CPI Luxembourg', '', year2)
        CPI2=column[4].getText()
        c2=re.sub('\%', '', CPI2)
        print y2, c2
        try :
            litnor.append([int(y2),float(c2)])
        except ValueError,e :
            continue
#********************************************************************

for row in tablestats.findAll('tr',{'class': 'tabledata2'}):
    column= row.findAll("td")
    x= column[0].find('a',class_=True)['title']
    print x
    if re.search("Average CPI inflation",x):
        print "Average"
        year1=column[0].getText()
        y1=re.sub('\CPI Luxembourg', '', year1)
        CPI= column[1].getText()
        c1=re.sub('\%', '', CPI)
        print y1,c1
        try :
            litavg.append([int(y1),float(c1)])
        except ValueError,e :
            continue

        year2=column[3].getText()
        y2=re.sub('\CPI Luxembourg', '', year2)
        CPI2=column[4].getText()
        c2=re.sub('\%', '', CPI2)
        print y2, c2
        try :
            litavg.append([int(y2),float(c2)])
        except ValueError,e :
            continue

    else:
        print "Not Average"
        year1=column[0].getText()
        y1=re.sub('\CPI Luxembourg', '', year1)
        CPI= column[1].getText()
        c1=re.sub('\%', '', CPI)
        print y1,c1
        try :
            litnor.append([int(y1),float(c1)])
        except ValueError,e :
            continue

        year2=column[3].getText()
        y2=re.sub('\CPI Luxembourg', '', year2)
        CPI2=column[4].getText()
        c2=re.sub('\%', '', CPI2)
        print y2, c2
        try :
            litnor.append([int(y2),float(c2)])
        except ValueError,e :
            continue














print "lit avergage:=" ,litavg
print "lit normal=:",litnor
litavg.sort()
litnor.sort()

for x, y in litavg :
    print >> favg, x, y

for x,y in litnor:
    print >> fannu, x, y


favg.close
fannu.close
    #print (column[0].text)

    #print row

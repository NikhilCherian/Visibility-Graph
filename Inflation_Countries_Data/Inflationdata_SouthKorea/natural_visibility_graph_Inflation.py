import os
import csv
import random
import string
import networkx as nx
import matplotlib
from matplotlib import pyplot
#from __future__ import division
tseries=[]



currentdirpath =os.getcwd()
filename =' Averageinflation_SouthKorea.csv'
file_path=os.path.join(currentdirpath, filename) #file_path to open

def get_file_path(filename):
    currentdirpath =os.getcwd()
    file_path=os.path.join(currentdirpath, filename)
    #print file_path
    return file_path


path= get_file_path('Averageinflation_SouthKorea.csv')
print path


natlist=[]
result=[]
def read_csv(filepath):
    with open(filepath, 'rU') as  csvfile:
        reader =csv.reader(csvfile,delimiter= ' ')
        for row in reader:
            #print row[1]
            natlist.append(row)
            print "nat=",natlist
        return natlist

lit=[]


def nat_visibility(tseries):
    for i in range(0,len(tseries)-1):
        (te,ye)=tseries[i]
        (tr,yr)=tseries[i+1]
        lit.append([te,tr])
    count=0
    print "join",tseries[1]
    for n in range(0,len(tseries)-1):
        (ta,ya)=tseries[n]
        for b in range(n+2,len(tseries)):
            (tb,yb)=tseries[b]
            visible=True
            for tc,yc in tseries:
                if tc>ta and tc<tb:
                    count=count+1;
                    nta=float(ta)
                    ntb=float(tb)
                    ntc=float(tc)
                    nya=float(ya)
                    nyb=float(yb)
                    nyc=float(yc)
                    tca=(ntc-nta)
                    tba=(ntb-nta)
                    t=tca/(tba*1.0)
                    yca=nyc-nya
                    eq=nyc-(nya+(nyb-nya)*t)
                    if eq>0.0:
                        visible=False

            if visible:
                lit.append([ta,tb])



                        #lit.append([tb,tc])
    print "lit=",lit
    print "count=",count

    return lit



def node_graph(tup):
    h=nx.Graph()
    h.add_edges_from(tup)
    print "edges:" ,h.edges()
    #%matplotlib inline
    BLUE="#99CCFF"
    nx.draw(h, node_color=BLUE,with_labels=True)
    print "Degree Distribution:",h.degree()
    print "Degree Centrality:",nx.degree_centrality(h)
    print "Betweenness Centrality : ",nx.betweenness_centrality(h)
    print "Betweenness Centrality Non-Normalized : ",nx.betweenness_centrality(h, normalized=False)
    print "Closeness Centrality:", nx.closeness_centrality(h)
    pyplot.show()


def tup_series(tup):
    print "Tup is here", tup[1],tup[2]
    n=1
    for magnitude in tup:
        tseries.append((n,magnitude))
        n=n+1
    print "Tseries = ", tseries
    return tseries

tup=read_csv(path)
#tseries =tup_series(tup)
print "tup is : =",tup
tseries=[]
tseries=tup
li=nat_visibility(tseries)

node_graph(li);
#print tup[0],tup[1]

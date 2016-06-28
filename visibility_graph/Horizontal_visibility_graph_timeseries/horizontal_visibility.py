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
filename =' graphdata.csv'
file_path=os.path.join(currentdirpath, filename) #file_path to open

def get_file_path(filename):
    currentdirpath =os.getcwd()
    file_path=os.path.join(currentdirpath, filename)
    #print file_path
    return file_path


path= get_file_path('timeseries.csv')
print path


natlist=[]
result=[]
def read_csv(filepath):
    with open(filepath, 'rU') as  csvfile:
        reader =csv.reader(csvfile)
        for row in reader:
            print row[1]
            natlist.append(row[1])
            print "nat=",natlist
        return natlist

lit=[]


def horizon_visibility(tseries):
    for i in range(0,len(tseries)-1):
        (ta,ya)=tseries[i]
        for n in range(i+1,len(tseries)):
            (tb,yb)=tseries[n]
            if(yb==ya):
                lit.append([ta,tb])
    print "lit=",lit


    return lit



def node_graph(tup):
    h=nx.Graph()
    h.add_edges_from(tup)
    print "hi"
    print "edges:" ,h.edges()
    #%matplotlib inline
    BLUE="#99CCFF"
    nx.draw(h, node_color=BLUE,with_labels=True)
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
tseries =tup_series(tup)


li=horizon_visibility(tseries)
print "li is :" , li
node_graph(li);
#print tup[0],tup[1]

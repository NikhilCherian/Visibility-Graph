import os
import csv
import random
import string
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
#from matplotlib import pylab as plt
#from __future__ import division
tseries=[]

mycategorydict={}



def mydict(n):
    mycategorydict[n]=n


    '''
    if n>1956 and n<1966:
        mycategorydict[n]=1
    elif n>1966 and n<1976:
        mycategorydict[n]=2
    elif n>1976 and n<1986:
        mycategorydict[n]=3
    elif n>1986 and n<1996:
        mycategorydict[n]=4
    elif n>1996 and n<2006:
        mycategorydict[n]=5
    else :
        mycategorydict[n]=6
        '''








currentdirpath =os.getcwd()
filename =' Averageinflation_GreatBritain.csv'
file_path=os.path.join(currentdirpath, filename) #file_path to open

def get_file_path(filename):
    currentdirpath =os.getcwd()
    file_path=os.path.join(currentdirpath, filename)
    #print file_path
    return file_path


path= get_file_path('Averageinflation_GreatBritain.csv')
#print path


natlist=[]
result=[]
def read_csv(filepath):
    with open(filepath, 'rU') as  csvfile:
        reader =csv.reader(csvfile,delimiter= ' ')
        for row in reader:
            #print row[0]
            mydict(int(row[0]))
            natlist.append(row)
            #print "nat=",natlist
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
    #print "lit=",lit
    #print "count=",count

    return lit

nod=[]
labels = {}

def node_graph(tup):
    h=nx.Graph()
    h.add_edges_from(tup)
    print "nodes:" ,h.nodes()
    for i in h.nodes():
        nod.append(int(i))

    print "nod =", nod
    print mycategorydict[1956]
    labels = {}

    #%matplotlib inline
    BLUE="#99CCFF"
    #nx.draw_spring(h, node_color=BLUE,with_labels=True)
    '''
    print "Degree Distribution:",h.degree()
    print "Degree Centrality:",nx.degree_centrality(h)
    print "Betweenness Centrality : ",nx.betweenness_centrality(h)
    print "Betweenness Centrality Non-Normalized : ",nx.betweenness_centrality(h, normalized=False)
    print "Closeness Centrality:", nx.closeness_centrality(h)
    '''
    print mycategorydict
    pos = nx.spring_layout(h)
    values = [mycategorydict.get(node, 0) for node in nod]
    print "values =",values
    jet = cm = plt.get_cmap('jet')
    cNorm  = colors.Normalize(vmin=0, vmax=max(values))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)


    f = plt.figure(1)
    ax = f.add_subplot(1,1,1)
    for label in mycategorydict:
        ax.plot([0],[0],
                color=scalarMap.to_rgba(mycategorydict[label]),
                label=label)

    #nx.draw_networkx(h,pos, cmap = jet, vmin=0, vmax= max(values),node_color=values,with_labels=True,ax=ax)

    labels=nx.draw_networkx_labels(h,pos)
    nodes = nx.draw_networkx_nodes(h, pos, node_size=100, node_color=values, cmap =     plt.cm.jet,
                               font_size=8, label=labels)

    edges = nx.draw_networkx_edges(h, pos ,alpha=0.8)
    #nx.draw_networkx_labels(h,pos,mycategorydict,font_size=10,font_color='r')

    plt.axis('off')
    f.set_facecolor('w')

    #plt.legend(loc=2, fontsize = 'xx-small')
    plt.colorbar(nodes)

    f.tight_layout()
    plt.show()


def tup_series(tup):
    print "Tup is here", tup[1],tup[2]
    n=1
    for magnitude in tup:
        tseries.append((n,magnitude))
        n=n+1
    #print "Tseries = ", tseries
    return tseries

tup=read_csv(path)
#tseries =tup_series(tup)
print "tup is : =",tup
tseries=[]
tseries=tup
li=nat_visibility(tseries)
print "mydict=",mycategorydict
node_graph(li)
#print tup[0],tup[1]

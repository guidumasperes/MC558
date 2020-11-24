#Classes to contruct and manipulate Graphs
from collections import defaultdict
from collections import OrderedDict 

class Graph:  
  def __init__(self):  
    self.graph = defaultdict(list) 

  # function to add an edge to graph and weight dict
  def addEdge(self,u,v,w,val):
    self.graph[u].append(v)
    w[(u,v)] = val

class Vertex:
  def __init__(self):
    self.name = None
    self.p = None
    self.rank = None

#kruskal and data structures
def make_set(x):
  x.p = x
  x.rank = 0

def link(x,y):
  if x.rank > y.rank:
    y.p = x
  else:
    x.p = y
    if x.rank == y.rank:
      y.rank = y.rank + 1

def find_set(x):
  if x != x.p:
    x.p = find_set(x.p)
  return x.p

def union(x,y):
  link(find_set(x),find_set(y))

def sort_edges(w):
  return OrderedDict(sorted(w.items(), key=lambda x: x[1]))

def mst_kruskal(G,w):
  A = []
  for u in G.graph:
    make_set(u)
  sorted_w = sort_edges(w)
  for e in sorted_w:
    if find_set(e[0]) != find_set(e[1]):
      A.append(e)
      union(e[0],e[1])
  return A

#main
u,v,w,x = Vertex(),Vertex(),Vertex(),Vertex()

u.name = 'u'
v.name = 'v'
w.name = 'w'
x.name = 'x'

G = Graph()

W = {}

G.addEdge(u, v, W, 4)
G.addEdge(u, x, W, 9)
G.addEdge(u, w, W, 3)
G.addEdge(v, u, W, 4)
G.addEdge(v, w, W, 2)
G.addEdge(v, x, W, 5)
G.addEdge(x, v, W, 5)
G.addEdge(x, u, W, 9)
G.addEdge(x, w, W, 1)
G.addEdge(w, x, W, 1)
G.addEdge(w, v, W, 2)
G.addEdge(w, u, W, 3)

mst = mst_kruskal(G,W)

for e in mst:
  print('(' + e[0].name + ',' + e[1].name + ')')
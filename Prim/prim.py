from collections import defaultdict 

#Classes to contruct and manipulate Graphs
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
    self.key = None

def fake_heapify(G):
  Q = {}
  Qaux = G.graph
  Qaux = [key for key in Qaux.keys()]
  for key in Qaux:
    Q[key] = key.key
  return Q

def fake_extract_min(Q):
  u = min(Q, key=Q.get) #extract-min of heap
  Q.pop(u)
  return u

def fake_decrease_key(Q,v):
  Q[v] = v.key

def mst_prim(G,w,r):
  for u in G.graph:
    u.key = float('inf')
    u.p = None
  r.key = 0
  A = [] #to return MST
  Q = fake_heapify(G)
  while len(Q) != 0:
    u = fake_extract_min(Q) #extract-min of heap
    if u.p != None: #insert in A
      A.append((u.p,u))
    for v in G.graph[u]:
      if v in Q and w[(u,v)] < v.key:
        v.p = u
        v.key = w[(u,v)]
        fake_decrease_key(Q,v) #update heap
  return A

#main
a,b,c,d,e,f,g,h,i = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

a.name = 'a'
b.name = 'b'
c.name = 'c'
d.name = 'd'
e.name = 'e'
f.name = 'f'
g.name = 'g'
h.name = 'h'
i.name = 'i'

G = Graph()

w = {}

G.addEdge(a, b, w, 4)
G.addEdge(a, h, w, 8)
G.addEdge(b, a, w, 4)
G.addEdge(b, h, w, 11)
G.addEdge(b, c, w, 8)
G.addEdge(c, b, w, 8)
G.addEdge(c, i, w, 2)
G.addEdge(c, f, w, 4)
G.addEdge(c, d, w, 7)
G.addEdge(d, c, w, 7)
G.addEdge(d, e, w, 9)
G.addEdge(e, d, w, 9)
G.addEdge(e, f, w, 10)
G.addEdge(f, e, w, 10)
G.addEdge(f, d, w, 14)
G.addEdge(f, c, w, 4)
G.addEdge(f, g, w, 2)
G.addEdge(g, f, w, 2)
G.addEdge(g, i, w, 6)
G.addEdge(g, h, w, 1)
G.addEdge(h, g, w, 1)
G.addEdge(h, b, w, 11)
G.addEdge(h, a, w, 8)
G.addEdge(i, c, w, 2)
G.addEdge(i, g, w, 6)
G.addEdge(i, h, w, 7)

mst = mst_prim(G,w,g)

for e in mst:
  print('(' + e[0].name + ',' + e[1].name + ')')
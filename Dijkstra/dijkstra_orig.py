#Classes to contruct and manipulate Graphs
from collections import defaultdict

class Graph:  
  def __init__(self):  
    self.graph = defaultdict(list) 

  #function to add an edge to graph and weight dict
  def addEdge(self,u,v,w,val):
    self.graph[u].append(v)
    w[(u,v)] = val

class Vertex:
  def __init__(self):
    self.d = float('inf')
    self.p = None
    self.name = None

#dijkstra and auxs
def path_printer(s, v):
  if s==v:
    print(s.name, end='')
  else:
    path_printer(s, v.p)
    print('->' + v.name, end='')

def initialize_single_source(G,s):
  for v in G.graph:
    v.d = float('inf')
    v.p = None
  s.d = 0

def relax(u,v,w,Q):
  if v.d > u.d + w[(u,v)]:
    v.d = u.d + w[(u,v)]
    v.p = u
    fake_decrease_key(Q,v)

#because im too lazy to implement real heap
def fake_heapify(G):
  Q = {}
  Qaux = G.graph
  Qaux = [key for key in Qaux.keys()]
  for key in Qaux:
    Q[key] = key.d
  return Q

def fake_extract_min(Q):
  u = min(Q, key=Q.get) #extract-min of heap
  Q.pop(u)
  return u

def fake_decrease_key(Q,v):
  Q[v] = v.d

#dijkstra itself 
def dijkstra(G,w,s):
  initialize_single_source(G,s)
  S = []
  Q = fake_heapify(G)
  while len(Q) != 0:
    u = fake_extract_min(Q)
    S.append(u)
    for v in G.graph[u]:
      relax(u,v,w,Q)

#main     
s,t,x,y,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
t.name = 't'
x.name = 'x'
y.name = 'y'
z.name = 'z'

G = Graph()

W = {}

G.addEdge(s, t, W, 10)
G.addEdge(s, y, W, 5)
G.addEdge(t, x, W, 1)
G.addEdge(t, y, W, 2)
G.addEdge(x, z, W, 4)
G.addEdge(z, x, W, 6)
G.addEdge(z, s, W, 7)
G.addEdge(y, z, W, 2)
G.addEdge(y, x, W, 9)
G.addEdge(y, t, W, 3)

dijkstra(G,W,s)

for v in G.graph:
  print(v.name + " = " + str(v.d))
  path_printer(s,v)
  print()
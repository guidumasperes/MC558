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
  d = {}
  for u in G.graph:
    d[u] = u.d
  return d

#exercise
def transpose_graph(G,w):
  GT = Graph()
  W = {}
  for u in G.graph:
    for v in G.graph[u]:
      GT.addEdge(v,u,W,w[(u,v)])
  return (GT,W)
      
def acha_preco(G,w,s,t,k):
  d_orig = dijkstra(G,w,s)
  result = transpose_graph(G,w)
  GT = result[0]
  w_GT = result[1]
  d_transp = dijkstra(GT,w_GT,t)
  preco = 0
  for u in G.graph:
    for v in G.graph[u]:
      if d_orig[u] + d_transp[v] + w[(u,v)] <= k:
        if w[(u,v)] > preco:
          preco = w[(u,v)]
  return preco

#main     
s,u,v,t,x = Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'

G = Graph()

W = {}

G.addEdge(s, u, W, 1)
G.addEdge(u, v, W, 7)
G.addEdge(v, x, W, 4)
G.addEdge(x, u, W, 10)
G.addEdge(v, t, W, 2)

print(acha_preco(G,W,s,t,31))
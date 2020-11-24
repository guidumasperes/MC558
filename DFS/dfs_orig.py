#Global variable to timestamp
tempo = 0

#Classes to contruct and manipulate Graphs
from collections import defaultdict

class Graph:  
  def __init__(self):  
    self.graph = defaultdict(list) 

  # function to add an edge to graph 
  def addEdge(self,u,v): 
    self.graph[u].append(v)

class Vertex:
  def __init__(self):
    self.color = 'white'
    self.d = float('inf')
    self.f = float('inf')
    self.p = None
    self.name = None

def dfs(G):
 for u in G.graph:
   u.cor = 'white'
   u.p = None
 for u in G.graph:
   if u.cor == 'white':
     dfs_visit(G,u)

def dfs_visit(G,u):
  global tempo
  tempo = tempo + 1
  u.d = tempo
  u.cor = 'grey'
  for v in G.graph[u]:
    if v.cor == 'white':
      v.p = u
      dfs_visit(G,v)
  u.cor = 'black'
  tempo = tempo + 1
  u.f = tempo

s,z,y,x,w,v,t,u = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
z.name = 'z'
y.name = 'y'
x.name = 'x'
w.name = 'w'
v.name = 'v'
t.name = 't'
u.name = 'u'

G = Graph()

G.addEdge(s, z)
G.addEdge(s, w)
G.addEdge(z, y)
G.addEdge(z, w)
G.addEdge(y, x)
G.addEdge(x, z)
G.addEdge(w, x)
G.addEdge(v, s)
G.addEdge(v, w)
G.addEdge(t, v)
G.addEdge(t, u)
G.addEdge(u, v)
G.addEdge(u, t)

dfs(G)
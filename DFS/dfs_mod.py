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
    self.p = None
    self.name = None

def dfs_mod(G):
 for u in G.graph:
   u.cor = 'branco'
   u.p = None
 for u in G.graph:
   if u.cor == 'branco':
     dfs_visit_mod(G,u)

def dfs_visit_mod(G,u):
  global tempo
  tempo = tempo + 1
  u.d = tempo
  u.cor = 'cinza'
  for v in G.graph[u]:
    if v.cor == 'branco':
      print('(' + u.name + ', ' + v.name + ')' + ' eh aresta da arvore')
      v.p = u.name
      dfs_visit_mod(G,v)
    elif v.cor == 'cinza':
      print('(' + u.name + ', ' + v.name + ')' + ' eh aresta de retorno')
    else:
      if u.d < v.d:
        print('(' + u.name + ', ' + v.name + ')' + ' eh aresta avanco')
      else:
        print('(' + u.name + ', ' + v.name + ')' + ' eh aresta cruzada')
  u.cor = 'preto'
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

dfs_mod(G)
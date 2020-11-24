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
    self.cor = 'white'
    self.d = float('inf')
    self.f = float('inf')
    self.p = None
    self.name = None

def dfs_mod(G,Ans):
 for u in G.graph:
   u.cor = 'white'
   u.p = None
 for u in list(G.graph): #orig: G.graph
   if u.cor == 'white':
     dfs_visit_mod(G,u,Ans)

def dfs_visit_mod(G,u,Ans):
  global tempo
  tempo = tempo + 1
  u.d = tempo
  u.cor = 'grey'
  for v in G.graph[u]:
    if v.cor == 'white':
      v.p = u
      dfs_visit_mod(G,v,Ans)
  u.cor = 'black'
  tempo = tempo + 1
  u.f = tempo
  Ans.append(u)
  
def topological_sort(G):
  Ans = []
  dfs_mod(G,Ans)
  Ans.reverse()
  return Ans

p,s,r,y,o,v = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

p.name = 'p'
s.name = 's'
r.name = 'r'
y.name = 'y'
o.name = 'o'
v.name = 'v'

G = Graph()

G.addEdge(p, s)
G.addEdge(p, o)
G.addEdge(s, r)
G.addEdge(r, y)
G.addEdge(y, v)
G.addEdge(o, s)
G.addEdge(o, r)
G.addEdge(o, v)

Ans = topological_sort(G)

for i in Ans:
  print(i.name)
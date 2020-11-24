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
    self.paths = 0

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

def find_paths(G,s,t):
  l = topological_sort(G)
  t.paths = 1
  for u in reversed(l):
    for v in G.graph[u]:
      u.paths = u.paths + v.paths
  return s.paths

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
G.addEdge(w, x)
G.addEdge(v, s)
G.addEdge(v, w)
G.addEdge(t, v)
G.addEdge(t, u)
G.addEdge(u, v)

ans = topological_sort(G)
for i in ans:
  print(i.name)
print()
print(find_paths(G,t,x))
print()
for i in G.graph:
  print(i.name + " = " + str(i.paths))
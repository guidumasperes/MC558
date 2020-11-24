#Global variable to timestamp
tempo = 0

#Classes to contruct and manipulate Graphs
from collections import defaultdict

class Graph:  
  def __init__(self):  
    self.graph = defaultdict(list) 

  # function to add an edge to graph 
  def addEdge(self,u,v,color,c): 
    self.graph[u].append(v)
    color[(u,v)] = c

class Vertex:
  def __init__(self):
    self.cor = 'white'
    self.d = float('inf')
    self.f = float('inf')
    self.p = None
    self.name = None
    self.valid_blue = None
    self.valid_red = None
    self.valid_paths = 0

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

def find_paths(G,color):
  l = topological_sort(G)
  azul ={}
  verm = {}
  valid = {}
  for u in G.graph:
    azul[u] = 0
    verm[u] = 0
  for u in reversed(l):
    for v in G.graph[u]:
      if color[(u,v)] == 'blue':
        azul[u] = azul[u] + azul[v] + verm[v] + 1
      elif color[(u,v)] == 'red':
        verm[u] = verm[u] + azul[v] + 1
    valid[u] = azul[u] + verm[u] + 1
  return valid

p,q,r,s,t,u,v,w,x,y,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

p.name = 'p'
q.name = 'q'
r.name = 'r'
s.name = 's'
t.name = 't'
u.name = 'u'
v.name = 'v'
z.name = 'z'
y.name = 'y'
x.name = 'x'
w.name = 'w'

G = Graph()

color = {}

G.addEdge(p, q, color, 'red')
G.addEdge(p, s, color, 'red')
G.addEdge(p, u, color, 'blue')
G.addEdge(q, r, color, 'red')
G.addEdge(q, s, color, 'blue')
G.addEdge(q, t, color, 'blue')
G.addEdge(r, s, color, 'blue')
G.addEdge(s, x, color, 'red')
G.addEdge(s, t, color, 'blue')
G.addEdge(s, v, color, 'blue')
G.addEdge(t, x, color, 'red')
G.addEdge(t, w, color, 'blue')
G.addEdge(u, v, color, 'red')
G.addEdge(u, w, color, 'red')
G.addEdge(u, y, color, 'blue')
G.addEdge(w, x, color, 'red')
G.addEdge(w, y, color, 'blue')
G.addEdge(x, y, color, 'red')
G.addEdge(x, z, color, 'blue')
G.addEdge(y, z, color, 'blue')

dic = find_paths(G,color)

print(end='             ')
for u in dic:
  print(u.name, end='  ')
print()

print(dic.values())
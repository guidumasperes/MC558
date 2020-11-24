#Global variable to timestamp in dfs_mod
tempo = 0
#Global variable to timestamp in dfs_mod_transp
tempo_mod = 0

#Classes to contruct and manipulate Graphs
from collections import defaultdict

class Graph:  
  def __init__(self):  
    self.graph = defaultdict(list) 

  #Function to add an edge to graph 
  def addEdge(self,u,v): 
    self.graph[u].append(v)

class Vertex:
  def __init__(self):
    self.color = 'white'
    self.d = float('inf')
    self.f = float('inf')
    self.p = None
    self.name = None

#DFS modded to return a vertex list sorted in cres order of u.f
def dfs_mod(G,Ans):
 for u in G.graph:
    u.cor = 'white'
    u.p = None
 for u in G.graph:
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

#Function to find the transpose of G, i.e., GT
def transpose_graph(G):
  GT = Graph()
  for u in G.graph:
    for v in G.graph[u]:
      GT.addEdge(v,u)
  return GT

#DFS modded to visit vertices in descres order
def dfs_mod_transp(G,SortedCres):
  Ans = []
  for u in G.graph:
    u.cor = 'white'
    u.p = None
  for u in reversed(SortedCres):
    if u.cor == 'white':
      T = Graph()
      dfs_visit_mod_transp(G,u,T)
      Ans.append(T)
      T = None
  return Ans

def dfs_visit_mod_transp(G,u,T):
  global tempo_mod
  tempo_mod = tempo_mod + 1
  u.d = tempo_mod
  u.cor = 'grey'
  for v in G.graph[u]:
    if v == u: #not sure about this
      v.p = u
      T.addEdge(u,v)
    if v.cor == 'white':
      v.p = u
      T.addEdge(u,v)
      dfs_visit_mod_transp(G,v,T)
  u.cor = 'black'
  tempo_mod = tempo_mod + 1
  u.f = tempo_mod

#Find SCC
def SCC(G):
  SortedCres = []
  dfs_mod(G,SortedCres)
  GT = transpose_graph(G)
  SCCS = dfs_mod_transp(GT,SortedCres)
  return SCCS

#Prepare graph and call SCC
a,b,c,d,e,f,g,h = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

a.name = 'a'
b.name = 'b'
c.name = 'c'
d.name = 'd'
e.name = 'e'
f.name = 'f'
g.name = 'g'
h.name = 'h'

G = Graph()

G.addEdge(e, a)
G.addEdge(a, b)
G.addEdge(b, c)
G.addEdge(d, c)
G.addEdge(c, d)
G.addEdge(b, e)
G.addEdge(b, f)
G.addEdge(e, f)
G.addEdge(g, f)
G.addEdge(f, g)
G.addEdge(c, g)
G.addEdge(g, h)
G.addEdge(d, h)
G.addEdge(h, h)

Ans = SCC(G)

count = 1
for component in Ans:
  print('SCC ' + str(count))
  for i in component.graph:
    for j in component.graph[i]:
      print(i.name + ' --> ' + j.name)
  count = count + 1
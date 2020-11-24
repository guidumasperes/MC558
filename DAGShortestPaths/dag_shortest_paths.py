#global variable for DFS
tempo = 0
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
    self.p = None
    self.name = None
    self.cor = 'white'
    self.d = float('inf')
    self.f = float('inf')

#topological-sort part
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

#dag part
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

def relax(u,v,w):
  if v.d > u.d + w[(u,v)]:
    v.d = u.d + w[(u,v)]
    v.p = u

def dag_shortest_paths(G,w,s):
  l = topological_sort(G)
  initialize_single_source(G,s)
  for u in l:
    for v in G.graph[u]:
      relax(u,v,w)

#main
r,s,t,x,y,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

r.name = 'r'
s.name = 's'
t.name = 't'
x.name = 'x'
y.name = 'y'
z.name = 'z'

G = Graph()

W = {}

G.addEdge(r, s, W, 5)
G.addEdge(r, t, W, 3)
G.addEdge(s, x, W, 6)
G.addEdge(s, t, W, 2)
G.addEdge(t, x, W, 7)
G.addEdge(t, y, W, 4)
G.addEdge(t, z, W, 2)
G.addEdge(x, z, W, 1)
G.addEdge(x, y, W, -1)
G.addEdge(y, z, W, -2)

dag_shortest_paths(G,W,s)

for v in G.graph:
  print('For ' + v.name + ' the path length is: ' + str(v.d))
  if v.d != float('inf'):
    print('And the path is: ')
    path_printer(s,v)
    print()
  print()
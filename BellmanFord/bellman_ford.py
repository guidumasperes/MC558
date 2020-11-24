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
    self.d = None
    self.p = None
    self.name = None

# bellman-ford and aux functions
def path_printer(s, v):
  if s==v:
    print(s.name, end='')
  else:
    path_printer(s, v.p)
    print('->' + v.name, end='')

def initialize_singue_source(G,s):
  for v in G.graph:
    v.d = float('inf')
    v.p = None
  s.d = 0

def relax(u,v,w):
  if v.d > u.d + w[(u,v)]:
    v.d = u.d + w[(u,v)]
    v.p = u

def bellman_ford(G,w,s):
  initialize_singue_source(G,s)
  for i in range(1,len(G.graph)-1):
    for e in w:
      relax(e[0],e[1],w)
  for e in w:
    if e[1].d > e[0].d + w[e]:
      return False
  return True 

#main
s,t,x,y,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
t.name = 't'
x.name = 'x'
y.name = 'y'
z.name = 'z'

G = Graph()

W = {}

G.addEdge(s, t, W, 6)
G.addEdge(s, y, W, 7)
G.addEdge(t, x, W, 5)
G.addEdge(t, z, W, -4)
G.addEdge(t, y, W, 8)
G.addEdge(x, t, W, -2)
G.addEdge(z, x, W, 7)
G.addEdge(z, s, W, 2)
G.addEdge(y, z, W, 9)
G.addEdge(y, x, W, -3)

if(bellman_ford(G,W,s)):
  print("The graph contains no negative-weight cycles that are reachable from the source")
else:
  print("The graph contains negative-weight cycles that are reachable from the source")

for v in G.graph:
  print(v.name + " = " + str(v.d))
  path_printer(s,v)
  print()
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

#BFS(Cormen)
def bfs(G,source):
  source.color = 'gray'
  source.d = 0
  source.p = None
  Q = []
  enqueue(Q,source)
  while len(Q) != 0:
    u = dequeue(Q)
    for v in G.graph[u]:
      if v.color == 'white':
        v.color = 'gray'
        v.d = u.d + 1
        v.p = u
        enqueue(Q,v)
    u.color = 'black'

#Function to print a path between two vertices
def path_printer(s, v):
  if s==v:
    print(s.name)
  else:
    path_printer(s, v.p)
    print(v.name)

#Functions to manipulate the Queue
def enqueue(Q,v):
  Q.append(v)

def dequeue(Q):
  return Q.pop(0)

s,a,b,c,d,e,f,g,h,i = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

#Just to make easy to print the path
s.name = 's'
a.name = 'a'
b.name = 'b'
c.name = 'c'
d.name = 'd'
e.name = 'e'
f.name = 'f'
g.name = 'g'
h.name = 'h'
i.name = 'i'

G = Graph()

G.addEdge(s, a)
G.addEdge(s, d)
G.addEdge(s, g)
G.addEdge(a, s)
G.addEdge(a, b)
G.addEdge(a, c)
G.addEdge(b, a)
G.addEdge(c, a)
G.addEdge(d, e)
G.addEdge(d, f)
G.addEdge(d, s)
G.addEdge(e, d)
G.addEdge(f, d)
G.addEdge(g, h)
G.addEdge(g, i)
G.addEdge(g, s)
G.addEdge(h, g)
G.addEdge(i, g)

bfs(G,s)
path_printer(s,i)
#graph1
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

#graph2
p,q,r,s,t = Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

p.name = 'p'
q.name = 'q'
r.name = 'r'
s.name = 's'
t.name = 't'

G = Graph()

color = {}

G.addEdge(p, q, color, 'red')
G.addEdge(p, t, color, 'red')
G.addEdge(q, r, color, 'blue')
G.addEdge(q, s, color, 'red')
G.addEdge(r, s, color, 'red')
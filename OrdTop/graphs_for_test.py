#graph 1
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

#graph 2
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
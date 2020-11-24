#graph 1
a,b,c,d,e,f,g,h,i = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

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

w = {}

G.addEdge(a, b, w, 4)
G.addEdge(a, h, w, 8)
G.addEdge(b, a, w, 4)
G.addEdge(b, h, w, 11)
G.addEdge(b, c, w, 8)
G.addEdge(c, b, w, 8)
G.addEdge(c, i, w, 2)
G.addEdge(c, f, w, 4)
G.addEdge(c, d, w, 7)
G.addEdge(d, c, w, 7)
G.addEdge(d, e, w, 9)
G.addEdge(e, d, w, 9)
G.addEdge(e, f, w, 10)
G.addEdge(f, e, w, 10)
G.addEdge(f, d, w, 14)
G.addEdge(f, c, w, 4)
G.addEdge(f, g, w, 2)
G.addEdge(g, f, w, 2)
G.addEdge(g, i, w, 6)
G.addEdge(g, h, w, 1)
G.addEdge(h, g, w, 1)
G.addEdge(h, b, w, 11)
G.addEdge(h, a, w, 8)
G.addEdge(i, c, w, 2)
G.addEdge(i, g, w, 6)
G.addEdge(i, h, w, 7)
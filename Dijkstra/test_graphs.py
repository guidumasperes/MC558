#G1
s,u,v,t,x,y,p,q = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'
y.name = 'y'
p.name = 'p'
q.name = 'q'

G = Graph()

W = {}

G.addEdge(s, u, W, 7)
G.addEdge(s, x, W, 6)
G.addEdge(s, p, W, 5)
G.addEdge(u, v, W, 10)
G.addEdge(x, y, W, 9)
G.addEdge(p, q, W, 8)
G.addEdge(v, t, W, 6)
G.addEdge(y, t, W, 7)
G.addEdge(q, t, W, 6)

print(acha_preco(G,W,s,t,22))

#G2
s,u,v,t,x,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'
z.name = 'z'

G = Graph()

W = {}

G.addEdge(s, z, W, 5)
G.addEdge(s, x, W, 10)
G.addEdge(z, v, W, 5)
G.addEdge(v, u, W, 1)
G.addEdge(x, u, W, 1)
G.addEdge(u, t, W, 1)

print(acha_preco(G,W,s,t,22))

#G3
s,u,v,t = Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'

G = Graph()

W = {}

G.addEdge(s, u, W, 1)
G.addEdge(u, v, W, 5)
G.addEdge(v, t, W, 3)
G.addEdge(v, s, W, 4)

print(acha_preco(G,W,s,t,22))

#G4
s,u,v,t,x,y = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'
y.name = 'y'

G = Graph()

W = {}

G.addEdge(s, v, W, 1)
G.addEdge(v, x, W, 2)
G.addEdge(x, u, W, 3)
G.addEdge(u, y, W, 4)
G.addEdge(y, v, W, 5)
G.addEdge(u, t, W, 6)

print(acha_preco(G,W,s,t,22))

#G5
s,u,v,t,x = Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'

G = Graph()

W = {}

G.addEdge(s, u, W, 1)
G.addEdge(u, v, W, 7)
G.addEdge(v, x, W, 4)
G.addEdge(x, u, W, 10)
G.addEdge(v, t, W, 2)

print(acha_preco(G,W,s,t,500))

#G6
s,u,v,t,x,y = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'
y.name = 'y'

G = Graph()

W = {}

G.addEdge(s, u, W, 1)
G.addEdge(u, v, W, 7)
G.addEdge(v, t, W, 2)
G.addEdge(v, x, W, 4)
G.addEdge(x, y, W, 10)
G.addEdge(y, u, W, 3)

print(acha_preco(G,W,s,t,60))

#G7
s,u,v,t,x,y,z = Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex(),Vertex()

s.name = 's'
u.name = 'u'
v.name = 'v'
t.name = 't'
x.name = 'x'
y.name = 'y'
z.name = 'z'

G = Graph()

W = {}

G.addEdge(s, u, W, 1)
G.addEdge(u, v, W, 7)
G.addEdge(v, x, W, 4)
G.addEdge(x, u, W, 10)
G.addEdge(v, t, W, 2)
G.addEdge(x, y, W, 3)
G.addEdge(x, z, W, 9)
G.addEdge(y, z, W, 20)
G.addEdge(z, u, W, 18)

result = SSP(G,W,s,t)

print(result[0])
print()
for e in result[1]:
  print(e[0].name + " " + e[1].name)
print()
for e in result[2]:
  print(e[0].name + " " + e[1].name)
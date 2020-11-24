class vertex:
  visit = False
  p = None
  adj = []
  name = None

def find_bip_odd(source):
  source.visit = True
  source.p = None
  Q = []
  bip = {}
  bip[source.name] = 'blue'
  enqueue(Q,source)
  while len(Q) != 0:
    u = dequeue(Q)
    for v in u.adj:
      if not v.visit:
        v.visit = True
        v.p = u
        if bip[v.p.name] == 'blue':
          bip[v.name] = 'red'
        else:
          bip[v.name] = 'blue'
        enqueue(Q,v)
      elif bip[u.name] == bip[v.name]:
        cycle = []
        stack = []
        x = u
        y = v
        while x != y:
          push(stack,x)
          enqueue(cycle,y)
          x = x.p
          y = y.p
        push(stack,x)
        while len(stack) != 0:
          enqueue(cycle,pop(stack))
        enqueue(cycle,v)
        print_cycle(cycle)
        return cycle
  return bip

def print_cycle(C):
  for i in C:
    print(i.name)

def path_printer(s, v):
  if s==v:
    print(s.name)
  else:
    path_printer(s, v.p)
    print(v.name)

def enqueue(Q,v):
  Q.append(v)

def dequeue(Q):
  return Q.pop(0)

def push(P,v):
  P.append(v)  

def pop(P):
  return P.pop(len(P)-1)

s,a,b,c,d,e = vertex(),vertex(),vertex(),vertex(),vertex(),vertex()

s.adj = [a]
a.adj = [s, b, c]
b.adj = [a, d]
c.adj = [a, d, e]
d.adj = [b, c, e]
e.adj = [c, d]

s.name = 's'
a.name = 'a'
b.name = 'b'
c.name = 'c'
d.name = 'd'
e.name = 'e'

G = [s,a,b,c,d,e]

result = find_bip_odd(s)
print(result)
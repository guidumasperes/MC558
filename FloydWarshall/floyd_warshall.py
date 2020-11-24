#Floyd-Warshall and predecessors
def floyd_warshall(W):
  n = len(W)
  D_bef = W
  for k in range(n):
    D_now = [[float('inf')]*n for x in range(n)]
    for i in range(n):
      for j in range(n):
        D_now[i][j] = min(D_bef[i][j],D_bef[i][k]+D_bef[k][j])
    D_bef = D_now
  return D_now
    
#main
W = [[float('inf')]*5 for x in range(5)]

W[0][0] = 0
W[0][1] = 3
W[0][2] = 8
W[0][4] = -4
W[1][1] = 0
W[1][3] = 1
W[1][4] = 7
W[2][1] = 4
W[2][2] = 0
W[3][0] = 2
W[3][2] = -5
W[3][3] = 0
W[4][3] = 6
W[4][4] = 0 

print(floyd_warshall(W))
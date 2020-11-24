#Floyd-Warshall and predecessors
def floyd_warshall_with_pred(W):
  n = len(W)
  D_bef = W
  P_bef = [[None]*n for x in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j or W[i][j] == float('inf'):
        P_bef[i][j] = None
      elif i != j or W[i][j] < float('inf'):
        P_bef[i][j] = i+1 #vertex start at 1
  print('for k = 0:')
  print(D_bef)
  print()
  print(P_bef)
  print()
  for k in range(n):
    D_now = [[float('inf')]*n for x in range(n)]
    P_now = [[None]*n for x in range(n)]
    for i in range(n):
      for j in range(n):
        D_now[i][j] = min(D_bef[i][j],D_bef[i][k]+D_bef[k][j])
        if D_bef[i][j] <= D_bef[i][k] + D_bef[k][j]:
          P_now[i][j] = P_bef[i][j]
        elif D_bef[i][j] > D_bef[i][k] + D_bef[k][j]:
          P_now[i][j] = P_bef[k][j]
    D_bef = D_now
    P_bef = P_now
    print('for k = ' + str(k+1) + ':')
    print(D_bef)
    print()
    print(P_bef)
    print()
  return (D_now, P_now)
    
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

result = floyd_warshall_with_pred(W)
print('In main:')
print(result[0])
print()
print(result[1])
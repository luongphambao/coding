from sys import stdin
r,c = map(int,stdin.readline().split())
l = []
for i in range(r):
  l.append(list(map(int,stdin.readline().split())))


for i in range(r):
  for j in range(c):
    l[i][j] = str(l[i][j])

max = []
  
for j in range(c):
  max.append(0)
  for i in range(r):
    if len(l[i][j]) >= max[j]:
      max[j] = len(l[i][j])
    else:
      max[j] = max[j]
for i in range(r):
  for j in range(c):   
    for m in range(max[j]-len(l[i][j])):
      print(" ", end = "")
    print(l[i][j],end = ' ')
  print("")
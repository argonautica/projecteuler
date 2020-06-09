temp = 0
sol = 0
for i in range(115, 1001):
  tempsol = 0
  for j in range(0, i):
    for k in range(0,i):
      for l in range(0,i):
        if(i + j + k ==i):
          if (l*l + k*k) == j*j:
            tempsol += 1
  if tempsol > sol:
    temp = i
    sol = tempsol
print(temp)
print(sol)

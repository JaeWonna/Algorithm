n = int(input())
lope = []
res = []

for _ in range(n):
    lope.append(int(input()))

lope.sort(reverse = True)

for i in range(n):
    res.append(lope[i]*(i+1))
print(max(res)) 

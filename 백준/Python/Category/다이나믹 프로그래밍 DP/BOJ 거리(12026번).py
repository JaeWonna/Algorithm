import sys
n=int(input())
block=str(input())
dp=[0]+[sys.maxsize]*n
def prev_word(s):
    if s=='B':
        return 'J'
    if s=='O':
        return 'B'
    if s=='J':
        return 'O'

for i in range(1, n):
    prev=prev_word(block[i])
    for j in range(i):
        if block[j]==prev:
            dp[i]=min(dp[i], dp[j]+(i-j)**2)
if dp[n-1]==sys.maxsize:
    print(-1)
else:
    print(dp[n-1])

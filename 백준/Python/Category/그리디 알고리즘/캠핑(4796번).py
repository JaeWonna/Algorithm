idx = 1

while True:
    L,P,V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    cnt = (V//P) * L
    cnt += min((V%P),L)
    
    print(f"Case {idx}: {cnt}")
    idx += 1

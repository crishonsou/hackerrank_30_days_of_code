def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    for x,y in zip(A,B):
        if x+y<k:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(twoArrays(k, A, B))

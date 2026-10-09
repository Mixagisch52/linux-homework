#!/opt/homebrew/bin/python3

alp = input().split()
n = int(input())
k = len(alp)
s = k**n
for i in range(s):
    q = ''
    numb = i
    for _ in range(n):
        r = numb % k
        q = alp[r] + q
        numb = numb // k
    print(q)


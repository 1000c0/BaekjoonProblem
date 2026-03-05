import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(n):
    swapped =  False
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            cnt += 1
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
            if k == cnt:
                print(min(a[j], a[j+1]), max(a[j], a[j+1]))
                exit()
    if not swapped:
        break
if k > cnt:
    print(-1)
x, y = map(int, input().split())
z = 100 * y // x
n = 0
left, right = 1, 10**9
ans = -1

if z >= 99:
        print(-1)
else:
    while left <= right and z < 99:
        mid = (left + right) // 2
    
        if z < (100 * (y + mid)) // (x + mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1

    print(ans)
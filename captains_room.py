k,arr = int(input()),list(map(int,input().split()))
rset = set(arr)
print(((sum(rset)*k)-(sum(arr)))//(k-1))

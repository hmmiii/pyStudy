def acc(n, res=0):
    if n == 0:
        return res
    return acc(n-1, n+res)

result = acc(50)

print(result)
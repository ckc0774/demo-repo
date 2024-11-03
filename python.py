def sum_n(n):
    s = 0
    for i in range(1,n+1):
        s=s+i*i
    return s
print(sum_n(10))

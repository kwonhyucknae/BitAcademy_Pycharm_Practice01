def sum(*args):
    ans=0
    for i in range(len(args)):
        ans+=args[i]
    return ans

print(sum(1,2,3))
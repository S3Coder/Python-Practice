def doMath(n):
    if n<=1:
        return n
    else:
        return n * doMath(n-1)


print(doMath(4))
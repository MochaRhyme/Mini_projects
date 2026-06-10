def permutation_calculate(n,r):
    res=1
    for i in range(n,n-r,-1):
        res*=i
    return res

def combination_calculate(n,r):
    res=1
    for i in range(1,r+1):
        res=res*(n-i+1)//i
    return res
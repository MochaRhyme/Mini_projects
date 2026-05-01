def isPrimeD(num:int):
    if num<=1:
        return False
    for i in range(int(num**0.5),1,-1):
        if num%i==0:
            return False
    return True

primeMemo=[2]
def isPrimeM(num:int):
    global primeMemo
    if num<primeMemo[-1]:
        return num in primeMemo
    for i in range(primeMemo[-1]+1,num+1):
        f=1
        for j in primeMemo:
            if i%j==0:
                f=0
                break
        if f:
            primeMemo.append(i)
    if num in primeMemo:
        return True
    else:
        return False

def isPrimeE(num:int):
    e=[True]*(num+1)
    e[0],e[1]=False,False
    for i in range(2,num+1):
        if not e[i]:
            continue
        for j in range(i+i,num+1,i):
            e[j]=False
    return e[num]

print(isPrimeE(7))
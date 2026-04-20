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
    if num<=1:
        return False
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

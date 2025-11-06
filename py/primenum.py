def isPrimeD(num:int):
    if num==1:
        return False
    if num<0:
        return None
    for i in range(num-1,1,-1):
        if num%i==0:
            return False
    return True

#todo : 소수 메모지에이션 구현
primeMemo=[2]
def isPrimeM(num:int):
    if num in primeMemo:
        return True
    if num==1:
        return False
    if num<0:
        return None
    
def digits_split(num):
    '''Returns a list containing the digits of the number split apart.'''
    if not isinstance(num,int):
        raise TypeError('expected int, got '+type(num).__name__)
    if num<0:
        raise ValueError('Negative number cannot be split by digit.')
    if num==0:
        return [0]
    result=[]
    while num:
        result.append(num%10)
        num//=10
    return list(reversed(result))
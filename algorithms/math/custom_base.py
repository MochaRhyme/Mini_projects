def decimal_to_n_base(decimal_num,n):
    if decimal_num==0:return '0'
    if n>62 or n<1:
        raise ValueError('N cannot be smaller than 1 or larger than 62.')
    if n==1:
        return '0'*decimal_num
    num_mapping='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    res=''
    while decimal_num>0:
        decimal_num,r=decimal_num//n,decimal_num%n
        res+=num_mapping[r]
    return res[::-1]

def base_1_to_decimal(base_num_one):
    s=set(base_num_one)
    if len(s)>2 or not isinstance(base_num_one,str):
        raise ValueError('This is not in base 1 form. It must be a string made up of only 0.')
    if s!={'0'}:
        raise ValueError('This is not in base 1 form. It must be a string made up of only 0.')
    return base_num_one.count('0')
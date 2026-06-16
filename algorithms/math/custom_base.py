def decimal_to_n_base(decimal_num,n):
    if decimal_num==0:return '0'
    if n>62:
        raise ValueError('n cannot be larger than 62.')
    if n==1:
        return '0'*decimal_num
    num_mapping='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    res=''
    while decimal_num>0:
        decimal_num,r=decimal_num//n,decimal_num%n
        res+=num_mapping[r]
    return res[::-1]

print(decimal_to_n_base(3,1))
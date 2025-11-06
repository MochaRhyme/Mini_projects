try:
    a=int(input("10진수 입력: "))
except ValueError:
    print("정수가 아닌데?")
    exit()
a_bin=bin(a)
print("2진수로는: "+a_bin)

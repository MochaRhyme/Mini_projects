try:
    import matplotlib.pyplot as plt
    view=1
except:
    print('matplotlib이 설치되어 있지 않음 : 시각화 코드는 동작하지 않습니다!')
    view=0
n=int(input('수 입력:'))
nT=n
Tstep=0
resT=[n]
while nT!=1:
    #콜라츠 추측의 일반적 표현인 T(n)값 계산
    if nT%2==0:
        print(f'{nT}는 짝수이므로...')
        nT=nT//2
        resT.append(nT)
    else:
        print(f'{nT}는 홀수이므로...')
        nT=3*nT+1
        resT.append(nT)
    Tstep+=1
    print(f'[{Tstep}번째에 {nT}로 변합니다.]')
print(resT)
if view:
    plt.plot(resT,color='blue',marker='o',label='T(n)')
    x=range(Tstep+1)
    plt.xticks(x)
    #this code by gemini---
    for i, value in enumerate(resT):
        plt.annotate(
            str(value),
            (x[i], resT[i]),
            xytext=(3, 0),
            ha='center'
        )
    #---
    plt.legend()
    plt.title(f'Collatz Conjecture at {n}')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()
try:
    import matplotlib.pyplot as plt
    view=1
except:
    print('matplotlib이 설치되어 있지 않음 : 시각화 코드는 동작하지 않습니다!')
    view=0
while True:
    try:
        n=int(input('수 입력:'))
        break
    except:
        print('숫자 형태로 입력하세요!')

nT=n
Tstep=0
resT=[n]
print('---일반 콜라츠 추측 계산---')
while nT!=1:
    #콜라츠 추측의 일반적 표현인 T(n)값 계산
    if nT%2==0:
        print(f'{nT} : 짝수이므로...',end=' ')
        nT=nT//2
        resT.append(nT)
    else:
        print(f'{nT} : 홀수이므로...',end=' ')
        nT=3*nT+1
        resT.append(nT)
    Tstep+=1
    print(f'[{Tstep}번째에 {nT}로 변합니다.]')
print(resT)

nTP=n
TPstep=0
resTP=[n]
print('---스텝 최적화 콜라츠 추측 계산---')
while nTP!=1:
    #콜라츠 추측의 스텝 최적화형(?)인 T'(n)값 계산
    if nTP%2==0:
        print(f'{nTP} : 짝수이므로...',end=' ')
        nTP=nTP//2
        resTP.append(nTP)
    else:
        print(f'{nTP} : 홀수이므로...',end=' ')
        nTP=(3*nTP+1)//2
        resTP.append(nTP)
    TPstep+=1
    print(f'[{TPstep}번째에 {nTP}로 변합니다.]')

if view:
    x=range(Tstep+1)
    plt.plot(resT,color='blue',marker='o',label='T(n)')
    plt.plot(resTP,color='orange',marker='o',linestyle='--',label='T\'(n)')
    # plt.xticks(x)
    #this code by gemini(copy from code below)---
    for i, value in enumerate(resTP):
        plt.annotate(
            str(value),
            (x[i], resTP[i]),
            color='orange',
            xytext=(0, -13),
            textcoords='offset points',
            ha='center',
            fontsize=8
        )
    #---
    #this code by gemini---
    for i, value in enumerate(resT):
        plt.annotate(
            str(value),
            (x[i], resT[i]),
            xytext=(0, 5),
            textcoords='offset points',
            ha='center',
            fontsize=8
        )
    #---
    plt.legend()
    plt.title(f'Collatz Conjecture at {n}')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()
    plt.close()
try:
    import matplotlib.pyplot as plt
    view=1
except:
    print('matplotlib is not installed : visualization code will not work!')
    view=0
while True:
    try:
        n=int(input('input intager:'))
        break
    except:
        print('Please input intager!')

nT=n
Tstep=0
resT=[n]
print('---T(n) : General Collatz Conjecture---')
while nT!=1:
    #콜라츠 추측의 일반적 표현인 T(n)값 계산
    if nT%2==0:
        print(f'{nT} is even :',end=' ')
        nT=nT//2
        resT.append(nT)
    else:
        print(f'{nT} is odd :',end=' ')
        nT=3*nT+1
        resT.append(nT)
    Tstep+=1
    print(f'changed {nT} in {Tstep} step')
print(resT)

nTP=n
TPstep=0
resTP=[n]
print('---T\'(n) : Step optimization of Collatz Conjecture---')
while nTP!=1:
    if nTP%2==0:
        print(f'{nTP} is even :',end=' ')
        nTP=nTP//2
        resTP.append(nTP)
    else:
        print(f'{nTP} is odd :',end=' ')
        nTP=(3*nTP+1)//2
        resTP.append(nTP)
    TPstep+=1
    print(f'changed {nTP} in {TPstep} step')
print(resTP)

print('\nmax from T(n) :',max(resT[1:]))

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
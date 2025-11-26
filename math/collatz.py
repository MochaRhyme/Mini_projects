def AE(string:object='',code:str='0'):
    if not isinstance(string,str):
        string=str(string)
    return '\x1b['+code+'m'+string+'\x1b[0m'

steps=[0,0,0]

def cc(l:list,m:str):
    while l[-1]!=1:
        if l[-1]%2==0:
            print(AE(f'{l[-1]}은/는 짝수','93')+'입니다. :',end=' ')
            l.append(l[-1]//2)
        else:
            print(AE(f'{l[-1]}은/는 홀수','93')+'입니다. :',end=' ')
            if m=='d':
                l.append(3*l[-1]+1)
            elif m=='p':
                l.append((3*l[-1]+1)//2)
            elif m=='pp':
                if 3*l[-1]-1 in l:
                    print(AE(f'[{steps[2]+1} 번째에 루프가 감지되어 종료합니다.]','91'))
                    break
                l.append(3*l[-1]-1)
        if m=='d':
            steps[0]+=1
            print(AE(steps[0],'93'),end=' ')
        elif m=='p':
            steps[1]+=1
            print(AE(steps[1],'93'),end=' ')
        elif m=='pp':
            steps[2]+=1
            print(AE(steps[2],'93'),end=' ')
        print(AE('번째에 ','93'),end='')
        print(AE(f'{l[-1]}(으)로 바뀝니다.','93'))

def vcc(l:list,color:str,linestyle:str,label:str,):
    plt.plot(l,color=color,marker='o',linestyle=linestyle,label=label)
    #this code by gemini---
    for i, value in enumerate(l):
        plt.annotate(
            str(value),
            (x[i], l[i]),
            color=color,
            xytext=(0, -13),
            textcoords='offset points',
            ha='center',
            fontsize=8
        )
    #---

try:
    import matplotlib.pyplot as plt
    view=1
except:
    print(AE('matplotlib이 설치되어 있지 않음 : 시각화 코드는 동작하지 않습니다!','93'))
    view=0
print(f'{AE('<콜라츠 추측>','93')}을 시뮬레이션합니다...')
while True:
    try:
        n=int(input('콜라츠 추측의 최초 값이 되는 자연수를 입력하세요:'))
        if n<0:
            raise
        break
    except:
        print(AE('입력한 것이 자연수가 아닙니다!','91'))


resT=[n]
print('\n---T(n) : 일반적인 콜라츠 추측---')
cc(resT,'d')
print(resT)

resTP=[n]
print('\n---T\'(n) : 실행 횟수를 고려한 콜라츠 추측---')
cc(resTP,'p')
print(resTP)

resTPP=[n]
print('\n---T\'\'(n) : 루프될 수도 있는 콜라츠 추측(3n-1)---')
cc(resTPP,'pp')
print(resTPP)

print('\nT(n)에서의 최대값 :',max(resT[1:]))

if view:
    x=range(max(steps)+1)
    plt.xticks(x)
    vcc(resTPP,'red','dotted','T\'\'(n)')
    vcc(resTP,'orange','--','T\'(n)')
    vcc(resT,'blue','solid','T(n)')
    plt.legend()
    plt.title(f'Collatz Conjecture at {n}')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()
    plt.close()
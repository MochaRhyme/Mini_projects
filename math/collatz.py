try:
    import matplotlib.pyplot as plt
    view=1
except:
    print('matplotlib is not installed : visualization code will not work!')
    view=0
while True:
    try:
        n=int(input('input natural number:'))
        if n<0:
            raise
        break
    except:
        print('Please input natural number')

steps=[0,0,0]

def cc(l:list,m:str):
    while l[-1]!=1:
        if l[-1]%2==0:
            print(f'{l[-1]} is even :',end=' ')
            l.append(l[-1]//2)
        else:
            print(f'{l[-1]} is odd :',end=' ')
            if m=='d':
                l.append(3*l[-1]+1)
            elif m=='p':
                l.append((3*l[-1]+1)//2)
            elif m=='pp':
                if 3*l[-1]-1 in l:
                    print(f'[loop detected in {steps[2]+1} step]')
                    break
                l.append(3*l[-1]-1)
        print(f'changed {l[-1]} in',end=' ')
        if m=='d':
            steps[0]+=1
            print(steps[0],end=' ')
        elif m=='p':
            steps[1]+=1
            print(steps[1],end=' ')
        elif m=='pp':
            steps[2]+=1
            print(steps[2],end=' ')
        print('step')

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

resT=[n]
print('\n---T(n) : General Collatz Conjecture---')
cc(resT,'d')
print(resT)

resTP=[n]
print('\n---T\'(n) : Step optimization of Collatz Conjecture---')
cc(resTP,'p')
print(resTP)

resTPP=[n]
print('\n---T\'\'(n) : Collatz Conjecture that can be looped---')
cc(resTPP,'pp')
print(resTPP)

print('\nmax from T(n) :',max(resT[1:]))

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
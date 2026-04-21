import sys
fiboseq=[]
lucaseq=[]
def seqsQuery(n:int,m:str):
    if not isinstance(n,int):
        return -1
    if m.lower()=='fibo':
        if len(fiboseq)==0:
            fiboseq.append(0)
            fiboseq.append(1)
        while len(fiboseq)-1!=n:
            fiboseq.append(fiboseq[len(fiboseq)-2]+fiboseq[len(fiboseq)-1])
        return fiboseq[n]
    elif m.lower()=='luca':
        if len(lucaseq)==0:
            lucaseq.append(2)
            lucaseq.append(1)
        while len(lucaseq)-1!=n:
            lucaseq.append(lucaseq[len(lucaseq)-2]+lucaseq[len(lucaseq)-1])
        return lucaseq[n]

def Query():
    oper=list(input().split())
    if oper[0]=='fibo':
        print(seqsQuery(int(oper[1]),'fibo'))
    elif oper[0]=='luca':
        print(seqsQuery(int(oper[1]),'luca'))
    elif oper[0]=='debug':
        print('fiboseq :',fiboseq)
        print('lucaseq :',lucaseq)
    elif oper[0]=='exit':
        print('[종료]')
        sys.exit()
    else:
        print('what?')
while True:
    Query()
from pathlib import Path
import inspect
import os

memopath=Path(__file__).resolve().parent/'memo.txt'
workingfor=Path(inspect.stack()[1].filename).name

def memoHandle():
    if not os.path.isfile(memopath):
        print('Error in memocore : memo.txt 파일이 memocore에 없거나, 이름이 바뀌었거나, 이동되었을 가능성이 있습니다.\n새로 생성합니다...')
        f=open(memopath,'w',encoding='utf-8')
        f.close()
        return False
    return True

def doIExistInMemo():
    if not memoHandle():
        return False
    with open(memopath,'r',encoding='utf-8') as f:
        items=f.readlines()
        for i in items:
            l=i.split(';')
            if l[0]==workingfor:
                return True
    return False

def save(l):
    if not memoHandle():
        return False
    with open(memopath,'w+',encoding='utf-8') as f:
        pass


def load(): 
    if not memoHandle():
        return False
    with open(memopath,'r',encoding='utf-8') as f:
        items=f.readlines()
        for i in items:
            l=i.split(';')
            if l[0]==workingfor:
                return l[1:]
    print('Error in memocore : 메모에는 이 코드를 위한 값이 없습니다. None이 반환됩니다.')
    return None

if __name__=='__main__':
    print(memopath)
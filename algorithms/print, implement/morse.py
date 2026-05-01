def interpret_morse(code:str):
    contents=[]
    morse_code_char={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.__':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.-.-.-':'.'}
    for i in code.split(' '):
        if len(i)==5:
            if i=='-----':
                contents.append('0')
                continue
            l=list(i)
            if l[0]=='.':
                contents.append(str(l.count('.')))
                continue
            elif l[0]=='-':
                contents.append(str(l.count('-')+5))
                continue
        elif i=='':
            contents.append(' ')
        else:
            contents.append(morse_code_char[i])
            continue
    return ''.join(contents)

print(interpret_morse(input()))
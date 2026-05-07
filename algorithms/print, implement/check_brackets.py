def check_brackets(s:str):
    paired_with={')':'(',']':'[','}':'{','>':'<'}
    stack=[]
    for i in s:
        if i in')]}>':
            if not stack or stack[-1]!=paired_with[i]:
                return False
            else:
                stack.pop()
        elif i in'([{<':
            stack.append(i)
    return len(stack)==0

if __name__=='__main__':
    t=input()
    print(check_brackets(t))
    print(check_brackets('(Hello) {<World}>'))
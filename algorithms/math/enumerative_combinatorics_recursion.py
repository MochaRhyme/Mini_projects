def permutation(elem,r,repetition=False,cur_permutation=None):
    if cur_permutation is None:cur_permutation=[]
    if len(cur_permutation)==r:
        print(*cur_permutation)
        return
    if repetition:
        for i in range(len(elem)):
            permutation(elem,r,repetition,cur_permutation+[elem[i]])
    else:
        for i in range(len(elem)):
            permutation(elem[:i]+elem[i+1:],r,repetition,cur_permutation+[elem[i]])

def combination(elem,r,repetition=False,start_i=0,cur_combination=None):
    if cur_combination is None:cur_combination=[]
    if len(cur_combination)==r:
        print(*cur_combination)
        return
    if repetition:
        for i in range(start_i,len(elem)):
            combination(elem,r,repetition,i,cur_combination+[elem[i]])
    else:
        for i in range(start_i,len(elem)):
            combination(elem,r,repetition,i+1,cur_combination+[elem[i]])
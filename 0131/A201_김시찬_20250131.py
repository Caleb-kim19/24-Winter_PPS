import sys

def solve(S):
    result = []
    temp = []
    inside_tag = False
    
    for i in range(len(S)):
        if S[i] == '<':
            if temp:
                result.append(''.join(temp[::-1]))
                temp = []
            inside_tag = True
            result.append('<')
        elif S[i] == '>':
            result.append(''.join(temp))
            temp = []
            inside_tag = False
            result.append('>')
        elif inside_tag:
            result.append(S[i])
        else:
            if S[i] == ' ':
                if temp:
                    result.append(''.join(temp[::-1]))
                    temp = []
                result.append(' ')
            else:
                temp.append(S[i])
    
    if temp:
        result.append(''.join(temp[::-1]))
    
    return ''.join(result)

S = input().strip()
print(solve(S))
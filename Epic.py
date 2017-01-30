def userInt(Prompt):
    print Prompt,
    N = int(raw_input())
    return N

def userString(Prompt):
    print Prompt,
    S = raw_input()
    return S
    
def repeatS(string_to_expand, CX):
   return (string_to_expand * ((CX/len(string_to_expand))+1))[:CX]
    
def userFloot(Prompt):
    print Prompt,
    F = raw_input()
    return F
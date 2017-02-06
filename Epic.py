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
    
def ReadTemps():
    file = open('temps.txt') 
    temps = []
    for line in file:
        line = line.strip() 
        line = float(line) 
        temps.append(line) 
    return temps

def calavg(temps, start, stop):
    total = 0 
    for i in range(start, stop):
        total = total + temps[i]
    avg = total/stop
    print avg
    
    
    
    
    
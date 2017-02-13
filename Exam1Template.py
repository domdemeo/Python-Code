# ------------------------------------------------------
# reads the speeds in the specified file (filename) 
# and returns them as a list of integers
# ------------------------------------------------------
def LoadNoRush():
    file = open('Exam1DataNotRush.txt') 
    NoRush = []                                      
    for line in file:
        line = line.strip() 
        line = float(line) 
        NoRush.append(line) 
    return NoRush

def LoadRush():
    file = open('Exam1DataRush.txt') 
    Rush = []                                      
    for line in file:
        line = line.strip() 
        line = float(line) 
        Rush.append(line) 
    return Rush
# ------------------------------------------------------    
# calculates and returns the average of the numbers 
# in the the specified list (l) 
# ------------------------------------------------------
def GetAverage(Rush, Number):                     
    total = 0      
    for i in range(0, Number):
        total = total + Rush[i]                  
    avg = total/Number
    
    return avg                                   

# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or # equal to maxSpeed 
# ------------------------------------------------------
def count(Rush,MaxSpeed, Number, Fine):                    
    count = 0                                      
    Rush1 = []  
    Rush1 = Rush[0 : 15] 
    
    for x in Rush1:                                 
        if x > MaxSpeed:                         
            count += 1  
    
    fines = (count * Fine)
    return [count ,fines]
    
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines 
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they 
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100. 
# 
# THE CORRECT OUTPUT IS: # 
# The average speed during rush hour was 63.47. 
# The average speed not during rush hour was 64.07. 
# There were 4 speeders during rush hour.  Total fine = $600 
# There were 6 speeders not during rush hour.  Total fine = $600 
# ------------------------------------------------------

def main():
   
    A = GetAverage(LoadRush(), 15)      
    B = count(LoadRush(), 69, 15, 150)         
    C = GetAverage(LoadNoRush(), 15)      
    D = count(LoadNoRush(), 69, 15, 100)
    
    print "The average speed during rush hour was %s" %A                                          #63.47.
    print "The average speed not during rush hour was %s" %C                                     #64.07. 
    print "There were "  "speeders during rush hour."  "Total fine = %s " %B                     #$600 
    print "There were "  "speeders not during rush hour."  "Total fine = %s" %D           #$600
    
# ------------------------------------------------------
# kick off the program by calling main
main()
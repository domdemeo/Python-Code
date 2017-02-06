def loadtemps():
    file = open('temps.txt') 
    temps = []                                      #load temps file into list 
    for line in file:
        line = line.strip() 
        line = float(line) 
        temps.append(line) 
    return temps

def calavg(temps, start, stop):                     # define start and stop 
    total = 0                                       # define total                     
    x = stop - start                                # finds range fixes 116 problem 
    for i in range(start, stop):                    # find list range for newe list
        total = total + temps[i]                    # creates new list and adds togetehr to get total of list

     # print x                                         #prints x for test 
    avg = total/x                                   # calcuates average
    return avg                                      #returns to main

def count(temps, start, stop):                      # define start stop
    count1 = 0                                      # define count value
    temps1 = []                                     # define new list 
    temps1 = temps[start:stop]                      # define new list values 
    for x in temps1:                                # number of values in temp positive list 
         if x > 0:                                  # cmpairs list values 
            count1 += 1                             # is true adds 1 to count
    return count1                                   # returns to main 
    
        
  
calavg(loadtemps(), 0, 81)                          # test code

count(loadtemps(), 0, 81)                           #test code

def main():                             #main function
    L1 = calavg(loadtemps(), 0, 81)         # calc the average od 0 to 81 in list 
    L2 = count(loadtemps(), 0, 81)          # finds number of positive terms 0 to 81
    L3 = calavg(loadtemps(), 81, 116)       # calc the average od 81 to 116 in list 
    L4 = count(loadtemps(), 81, 116)        # finds number of positive terms 81 to 116
    
    print "During the first 81 years, the average deviation from the temperature anomaly is %s" %L1
    print "During the first 81 years, %s " % L2 + "had a positive temperature anomaly"
    print "During the last 35 years, the average deviation from the temperature anomaly is %s" %L3
    print "During the last 35 years, %s " %L4 + "had a positive temperature anomaly"

main()




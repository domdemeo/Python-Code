def CubeTimes(filename, low, high):
    cubelist0 = []
    #separates the file and adds the values in the dictionary
    for line in open(filename):
        temp = line.split(",")
        cubeplayer = temp[0].strip()
        playertime = float(temp[1].strip())
        #if the name of the player is in the file then it will add the player time also
        if(playertime > low and playertime < high):
            cubelist0.append(cubeplayer)
        
    return (cubelist0)
    
def printresults(array):
     for cubeplayer in array: 
         print cubeplayer

def main():
    cubelist1 = CubeTimes("CubeTimes.txt", 0.00, 9.99)
    cubelist2 = CubeTimes("CubeTimes.txt", 10.00, 19.99)
    cubelist3 = CubeTimes("CubeTimes.txt", 20.00, 29.99)
    cubelist4 = CubeTimes("CubeTimes.txt", 30.00, 39.99)
    cubelist5 = CubeTimes("CubeTimes.txt", 40.00, 59.99)
    cubelist6 = CubeTimes("CubeTimes.txt", 60.00, 9999.99)
    
    print "Cube heads (0 - 9.99)" 
    printresults(cubelist1) 
    
    print ""
    
    print "Square Master (10 - 19.99)"
    printresults(cubelist2) 
    
    print ""
    
    print "Advanced Twister (20 - 29.99)" 
    printresults(cubelist3)

    print ""
    
    print "Intermediate Turner (30 - 39.99)"
    printresults(cubelist4)
    
    print ""
    
    print "Average Mover (40 - 59.99)" 
    printresults(cubelist5)
    
    print ""
    
    print "Pathetic (60 and Above)"
    printresults(cubelist6)
main()
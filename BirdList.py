def countBirds(filename):
    birdnames = {}
    #separates the file and adds the values in the dictionary
    for line in open(filename):
        temp = line.split(",")
        bird = temp[0].strip()
        count = int(temp[1].strip())
        #if the name of the bird is in the file then it will add the values for it
        if bird in birdnames:
            birdnames[bird].append(count)
        #otherwise it will add the bird in the dictionary
        else:
            birdnames[bird] = [count]
    #creates new dictionary so that the for loop can add the sum of keys in the first dictionary
    sumofbirds = {}
    for key in birdnames:
        sumofbirds[key] = sum(birdnames[key])
    return sumofbirds
  
    

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    
    print "Enter the name of the bird you want to check: "
    
    #turns the first letter of each word into a capital one
    userinput = raw_input().upper().title()
    
    print "I have seen that bird %s times" %d[userinput]
  

def main():
    askUser(countBirds("birds.txt"))
     
main()

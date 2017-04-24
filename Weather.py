import Epic 
import json
import urllib2

def Readurl():
    
    Location = Epic.userString("Please enter a zip code or city name for the weather you want to check")
    print " "
    url = 'https://api.apixu.com/v1/current.json?key=d958be8e71044c20bf822757172404&q=' + Location
    JsonText = urllib2.urlopen(url).read()
    ApixuData = json.loads(JsonText)
    
    return ApixuData

def Print(ApixuData):
    
        print "The weather in %s, %s is Currently" % (ApixuData['location']['name'],ApixuData['location']['region'])
        print "%s and the Tempture is Currently %s degrees (F)." % (ApixuData['current']['condition']['text'],ApixuData['current']['temp_f'])
        print "It actually feels like it is %s (F)." % ApixuData['current']['feelslike_f']
        
        print " "

        return Print
        
def main():
    Run = True
    while Run == True:  
        Print(Readurl())
        repeat = Epic.userString("Do you want to check another location? (yes/no):")
        print " "
        if repeat == 'no':
            Run = False
        if repeat == 'yes':
            Run = True
main()

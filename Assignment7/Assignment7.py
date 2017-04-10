import Epic
import json

def ReadJson():
    JsonText = ""
    File = open('Classes.json')
    for line in File:                       #reads in Json and Strips each lines and adds it to a dictory
        line = line.strip()
        JsonText = JsonText + line
    Classes = json.loads(JsonText)
    
    return Classes

def UserInput(Classes):                         #Ask for user input and then prints out class name Profesor and location 
    print "Bowman Number Search"
    print "Please Enter One of the Following Completely Bowman Hall 101, 102, 103, 104, 105"
    Room = Epic.userString("Enter a Bowman Room Number:")
    for Class in Classes:
        if Class["Location"] == Room:
            print "Location: %s" % Class["Location"]
            print "Class: %s"  % Class["Class"]
            print "Time: %s" % Class["Time"]
            

def main():
    UserInput(ReadJson())               #calls upon user input and file read to inorder to run   
        
main()
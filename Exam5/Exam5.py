import Epic
import json

def ReadJson():
    JsonText = ""
    File = open('PetStore.json')
    for line in File:                       #reads in Json and Strips each lines and adds it to a dictory
        line = line.strip()
        JsonText = JsonText + line
    PetStore = json.loads(JsonText)
    return PetStore

def PetStoreSearch(Term, Search):
    Term = Term.title()
    Search= Search.title()
    PetStoreFile = ReadJson()
    if Search == "Category":                                
        for product in PetStoreFile:
            if product["Category"] == Term:
                print "%s - $%s" % (product["Product"], product["Price"])       #Prints out either category or keyword you searched for along with the product under that category and price 
    
    if Search == "Keyword":
        for product in PetStoreFile:
            if Term in product["Product"]:
               print "%s - $%s" % (product["Product"], product["Price"])
               
def main():
    String = Epic.userString("Please Enter (c) or (k) to Search by category or keyword ?")
    Search = ""
    if String.lower() =='c':
        Search = "Category (Food, Toys, Furniture)"
        Term = Epic.userString("Enter a %s:" % Search)              #checks if c and then searches for what ever category your search for
        PetStoreSearch(Term, Search)
    
    if String.lower() == 'k':
        Search = "Keyword"
        Term = Epic.userString("Enter a %s:" % Search)           #checks if Keyword and then searches for what ever Keyword your search for
        PetStoreSearch(Term, Search)
main()
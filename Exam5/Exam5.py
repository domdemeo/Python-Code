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
                print "%s - $%s" % (product["Product"], product["Price"])
    if Search == "Keyword":
        for product in PetStoreFile:
            if Term in product["Product"]:
               print "%s - $%s" % (product["Product"], product["Price"])
    
def main():
    String = Epic.userString("Please Enter (c) or (k) to Search by category or keyword ?")
    Search = ""
    if String.lower() =='c':
        Search = "category"
        Term = Epic.userString("Enter a %s:" % Search)
        PetStoreSearch(Term, Search)
    if String.lower() == 'k':
        Search = "keyword"
        Term = Epic.userString("Enter a %s:" % Search)
        PetStoreSearch(Term, Search)
    
main()
import Epic 
import os

def ReadFiles():                    #reads in files and contents them capatizes it so it wont miss any words
    FileList = []
    Files = os.listdir('.')
    for f in Files:
        if '.txt' in f:
            FileList.append(f)
    FileContentsFinal = {}
    
    for f in FileList:
        CapFile = open(f)
        CapLine = []
        for line in CapFile:
            CapLine.append(line.strip().upper())
        FileContentsFinal[f] = CapLine
    
    return FileContentsFinal

def SearchFiles(Word, FileContentsFinal):
    Count = 0
    FoundWords = []
    for f in FileContentsFinal:
        for line in FileContentsFinal[f]:               #looks at each line in each final file dicetory to find words
            if Word in line:
                FoundWords.append(f + ': ' + line)          #adds where word was found and file and prints out each
                Count += 1
    print 'This Word was Found %s Number of Times.' % Count             #word final count
    return FoundWords

def main():
    FileContentsFinal = ReadFiles()             #reads files captizesa and then has user enter word and them captizes it anf them searches file contencts for the word
    Word = Epic.userString('Please Enter a Search Word: ')
    Searched = SearchFiles(Word.upper(), FileContentsFinal)
    for s in Searched:
        print s
    
main()
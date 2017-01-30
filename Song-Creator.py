import Epic


print "--Welcome to Dom's Song Creator--" 
print

SongN = Epic.userString("Enter the Your Song's Name:")
V1 = Epic.userString("Enter the Your Song's First Verse:")
V2 = Epic.userString("Enter the Your Song's SecondVerse:")
V3 = Epic.userString("Enter the Your Song's ThirdVerse:")
V4 = Epic.userString("Enter the Your Song's FourthVerse:")
C = Epic.userString("Enter the Your Song's Chorus:")
CX = Epic.userInt("Enter the Number of Times You Want the Chorus to Repeat:")

C1 = C + " " 
CFull = (C1 * CX)
C2 = C + ", " 
CC = (C2 * CX)
SongList = ("'V1-1R', 'C1-1R', 'V2-1R', 'C2-1R', 'V3-1R', 'C3-1R', 'V4-1R', 'C4-1R', '--One More Time--' "
            "'V1-1R', 'C1-1R', 'V2-1R', 'C2-1R', 'V3-1R', 'C3-1R', 'V4-1R', 'C4-1R',")
print "-----------------------------"
print SongN
print "-----------------------------"

SongList = SongList.replace("V1-1R" , V1)
SongList = SongList.replace("C1-1R" , CFull)
SongList = SongList.replace("V2-1R" , V2)
SongList = SongList.replace("C2-1R" , CFull)
SongList = SongList.replace("V3-1R" , V3)
SongList = SongList.replace("C3-1R" , CFull)
SongList = SongList.replace("V4-1R" , V4)
SongList = SongList.replace("C4-1R" , CFull)

print SongList
print "-----------------------------------------------------------------------------------------------------------------"

print V1
print CC
print V2
print CC
print V3
print CC
print V4
print "--One More Time--"
print V1
print CC
print V2
print CC
print V3
print CC
print V4


  
  
  





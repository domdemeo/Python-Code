import Epic


print "--Welcome to Dom's Song Creator--" 
print

SongN = Epic.userString("Enter Your Song's Name:")
V1 = Epic.userString("Enter Your Song's First Verse:")
V2 = Epic.userString("Enter Your Song's SecondVerse:")
V3 = Epic.userString("Enter Your Song's ThirdVerse:")
V4 = Epic.userString("Enter Your Song's FourthVerse:")
C = Epic.userString("Enter Your Song's Chorus:")
CX = Epic.userInt("Enter the Number of Times You Want the Chorus to Repeat:")

C1 = C + " " 
CFull = (C1 * CX)

SongList = []
print "-----------------------------"
print SongN
print "-----------------------------"

SongList.append(V1)
SongList.append(C * CX)
SongList.append(V2)
SongList.append(C * CX)
SongList.append(V3)
SongList.append(C * CX)
SongList.append(V4)
SongList.append(C * CX + C)
SongList= SongList*2
SongList.insert (8, "--One More Time--")


print SongList
print "-----------------------------------------------------------------------------------------------------------------"

for x in SongList:
  print (x)





# This is a program to concatenate three strings together, create and store it on one line in the text file.
 InputData():
  CDTitle = ""
  CDArtist = ""
  CDLocation= ""
  Lineoftext=""
  CDTitle = input("Enter the title of the CD ")
  CDArtist = input("Enter the name of the Artist ")
  CDLocation = input("Please enter the location of the CD ")
  Lineoftext = CDTitle + CDArtist + CDLocation
  print(Lineoftext)
  FileHandle.write(Lineoftext)
#main
FileHandle = open("C:\work\python\MyMusic.txt",'w')
InputData()                     
FileHandle.close()

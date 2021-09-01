def InputData():
    while CDTitle!= "##"
        CDTitle = input("Enter the title of the CD")
        CDArtist = input("Enter the name of the Artist")
        CDLocation = input("Please enter the location of the CD")
        Lineoftext = CDTitle + CDArtist + CDLocation
        FileHandle = open("MyMusic.TXT","w")
        FileHandle.write(Lineoftext)
                      
    

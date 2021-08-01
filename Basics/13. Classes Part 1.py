class Song:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration
    
    def showSong(self):
        return "Name: "+self.name+"\nGenre: "+self.genre+"\nDuration: "+self.duration
    
    def showParticularGenre(self, genre):
        if self.genre == genre:
            return self.name
        else:
            return False    

countryroad = Song("Country Roads","Country Song","3m")
blowingwind = Song("Blowing in the wind","Folk","2m 10s")

print(countryroad.showSong())
print(blowingwind.showSong())
print(countryroad.showParticularGenre("Folk"))
print(blowingwind.showParticularGenre("Folk"))

# The getattr(obj, name[, default]) − to access the attribute of object.

# The hasattr(obj,name) − to check if an attribute exists or not.

# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

# The delattr(obj, name) − to delete an attribute.
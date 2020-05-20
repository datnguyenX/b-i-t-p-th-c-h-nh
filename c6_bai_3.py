class Nguoi(object):
    def getGendder( self ):
     return "Unknown"
class Nam(Nguoi):
    def getGender( self ):
     return "Nam"
class Nu(Nguoi):
    def getGendef( self ):
     return "Nu"
aNam = Nam
aNu = Nu
print(aNam.getGender())
print(aNu.getGender())

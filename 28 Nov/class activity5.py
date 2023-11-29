class Ship:
    def __init__(self, name, color):
        self.name=name
        self.color=color
        
    def say_ship(self):
        print ("The ship are {} and color is {} ".format(self.name , self.color))
        
    def area_ship(self):
        print ("Area = {} ".format(self.name , self.color))

  
class Circal(Ship):
    def __init(self, name, color,r):
        super().__init__( name, color)
        self.r=r
    
    def area_ship(self):
        area =(3.14*(self.r**2))
        return area 

    def say_ship(self):
        return("The ship are {} and color is {} ".format(self.name , self.color))
        
   
class Squir(Ship):
    def __init(self, name, color,l):
        super().__init__(name, color)
        self.l=l
    def area_ship2(self):
        area2 =self.l**2
        return area2
    
    def say_ship(self):
        return("The ship are {} and color is {} ".format(self.name,self.color))
    
                      
p1= Ship("yelow", "sh2")
p2= Squir("squir", "Pink")
s1= Circal("circl", "Yellow")
print(p1)
print(p2)
print(s1)
print ("Area= ", s1.area_ship())
print ("Area=  ", p2.area_ship2())
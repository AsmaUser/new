class Person:
    #attrapute for class:
    #salf: that atrabute returen to this class
    def __init__(self,name,age):
        self.name=name
        self.age= age
peron= Person("Asma", 23)
#print (peron)
#The output are reprsent the address in memory
#print (type(peron))
#The output represnt the type
print(peron.name)
print(peron.age)
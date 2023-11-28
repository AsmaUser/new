class Person:
    num_of_prson = 0
    #age = 22: defult value 
    def __init__(self,name,age=22):
        self.name=name
        self.age= age
        Person.num_of_prson +=1
    def __str__(self):
        return "hello {} you are {} yearsold".format(self.name, self.age)
    def talk(self):
        return "{} is talking".format(self.name)
peron= Person("Asma", 23)
peron2 = Person("aya", 23)
peron3= Person("reem")
print (peron3.num_of_prson)
print (peron3.age)
print (peron3.talk())

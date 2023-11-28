class Person:
    num_of_prson = 0
    #age = 22: defult value 
    def __init__(self,name,age=22):
        self.__name=name
        self.__age= age
        Person.num_of_prson +=1
    def set_name(self, new_name):
        self.__name = new_name
    def __str__(self):
        return "hello {} you are {} years old".format(self.__name, self.__age)
    def talk(self):
        return "{} is talking".format(self.name)
peron= Person("Asma", 23)
peron2 = Person("Aya", 23)
print (peron2)
peron3= Person("Reem")
peron2.set_name("Arya")
print (peron2)
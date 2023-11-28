class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say_hi(self):
        print ("hello {} from parant class ".format(self.name))
class Student(Person):
    def __init(self, name, age):
        super().__init__()
    def say_hi(self):
        print ("hello {} from student class ".format(self.name))
p1= Person("Aya", 22)
s1= Student("asma", 14)
p1.say_hi()
s1.say_hi()
        
#class person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #an instance introduce
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Creating an instance of the Person class
person1 = Person("valary", 21, "Female")
person2 = Person("sheldon",11,"male")
# Introducing the person
person1.introduce()
person2.introduce()
from Common.mammal import Mammal

# child class
class Dog(Mammal):

    legs = 5
    eyes = 2

    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print('Whoof, Whoof')

    # This is a static method, meant to be called directly from the class
    @staticmethod
    def walk():
        print("I am walking")

Clifford = Dog('Clifford', 2, 'Huskie')

Mammal.bio()
Dog.bio()
Clifford.bio()

# print(Clifford.feeds_milk)
# print(Dog.feeds_milk)
# print(Mammal.feeds_milk)
# print(message)
# say_hello()
# Dog.walk()
# Clifford.walk()

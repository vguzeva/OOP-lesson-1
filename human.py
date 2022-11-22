class Human: 
    legs = 2
    eyes = 2
    hands = 2
    fingers = 10

    def __init__(self, race, language) -> None:
        self.race = race
        self.language = language       

    def bio(self):
        print(f'Thank you for letting me in the class. My race is {self.race} and I speak {self.language}')

Steve  = Human('White', 'English')
John = Human('Asian', 'Mandarin')

Steve.bio()
John.bio()

# print(Steve.race)
# print(Steve.language)
# print(John.language)

# print(Human.language)





# John.legs = 1

# print(Steve.legs)
# print(John.legs)

# Human.fingers = 20

# print(Steve.fingers)




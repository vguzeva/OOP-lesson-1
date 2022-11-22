# create a class
class Employee:
    # class attributes
    os = 'Windows 2010'
    work_style = 'remote'
    hourly_salary = 15

    # Constructor method / initializer
    #build th object    
    def __init__(self, role, is_manager, location = 'New York'):
        self.role = role
        self.is_manager = is_manager
        self.location = location

    def bio(self):
        print(f'Hello! I am a {self.role} and I amd located in {self.location} branch')

# create object
Marian = Employee('Developer', False, 'Singapore')
Bob = Employee('QA', True)

print(Marian.bio())
print(Bob.bio())


# print(Marian.location)
# print(Bob.location)

# print(Marian.role)
# print(Bob.is_manager)
# print(Bob.role)




# Employee.hourly_salary = 16.75
# Marian.hourly_salary = 30
# Employee.hourly_salary = 18

# Employee.os = 'Linux'

# print(Bob.hourly_salary)
# print(Marian.hourly_salary)
# print(Marian.os)
# print(Bob.work_style)

# print(Bob.os)
# print(Marian.os)



# print(Marian)
# print(type(Bob))
# print(isinstance(Marian, Employee))
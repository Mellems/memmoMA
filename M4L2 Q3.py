
# create class call Restaurant
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 00
# create some functions for Restaurant
    def describe_restaurant(self):
        msg = f"{self.name} is awesome and has {self.cuisine_type}."
        print(f"\n{msg}")
    def open_restaurant(self):
        msg = f"{self.name} is NOW OPEN!!" 
        print(f"\n{msg}")
# creates a base for amount served and then and incrament to show progression
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, more_people_served):
        self.number_served += more_people_served

#creating IceCreamStand class that inherits the Restaurant() class
class IceCreamStand(Restaurant):
# when defining function make sure the cuisine_type  is specified in the parameters
    def __init__(self, name, cuisine_type = "IceCream"):
        super().__init__(name, cuisine_type)
        self.flavors = []
    def displays_flavors(self):
        print(f"This is the list of flavors: ")
        for flavor in self.flavors:
            print(f" {flavor}")

# make object name for example to plug into the function
ash = IceCreamStand("ASH's IceCream" )
# make a object list of flavors and use function displays_flavors
ash.flavors = ["strawberry", "banana", "kiwi", "pineapple"]
#print(ash.flavors)

# call back the object information use made using the fuctions in the class IceCreamStand(Restaurant)
ash.describe_restaurant()
ash.displays_flavors()

x = " "
print(x)
#create a class for an user with information about the user in the parameter
class User():
    def __init__(self, first_name, last_name, ID_number,
                 phone_number, email_address, user_age):
        self.first = first_name.title()
        self.last = last_name
        self.id = ID_number
        self.phone = phone_number
        self.email = email_address
        self.age = user_age
        self.login_attempts = 0
# create function to describe a user , greet a user.
    def describe_user(self):
        print(f" {self.first} {self.last}")
        print(f" ID:{self.id} ")
        print(f" phone:{self.phone} ")
        print(f" email:{self.email} ")
        print(f" age:{self.age} ")
    def greet_user(self):
        greet = f"Hello {self.first}, welcome to the company!"
        print(f"\n{greet}")
# create functions to show the amount of attepmts a user login and reset the attempts.
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

# create another class for Admin type users there inherets the functionsf from User() class. 
class Admin(User):
    def __init__(self, first_name, last_name, ID_number,
                 phone_number, email_address, user_age):
        super().__init__(first_name, last_name, ID_number,
                         phone_number,email_address, user_age)
        self.privileges = Privileges()

# create class for privileges a user has
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print(f"\nThis is a list of privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f" {privilege}".title())
        else:
            print("user does not have privileges.".title())

Emilio = Admin("emilio", "salazar", "15", "682", "emiliosalaza15@gmail.com", "21")

Emilio.describe_user()

# call object to show privileges and if the user does not have priviliges
Emilio.privileges.show_privileges()

# call object list of what privileges the user has
Emilio_privileges = [
    "can create database",
    "can delet database",
    "can ban user from database",
    ]
# call object to show the user has privileges
Emilio.privileges.privileges = Emilio_privileges
Emilio.privileges.show_privileges()



















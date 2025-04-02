#create class 
class Restaurant():
# create values for the object and define the function for each value.
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 00
    def describe_restaurant(self):
        msg = f"{self.name} is awesome and has {self.cuisine_type}."
        print(f"\n{msg}")
    def open_restaurant(self):
        msg = f"{self.name} is NOW OPEN!!" 
        print(f"\n{msg}")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, more_people_served):
        self.number_served += more_people_served

restaurant = Restaurant("basic", "outline")
# call back the object restraurant
restaurant.describe_restaurant()

# define the incremates for people being served throughout the day using class Restaurant
print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(125)
print(f"Number of people that have been served: {restaurant.number_served}")

restaurant.increment_number_served(200)
print(f"Toltal number of customers served today: {restaurant.number_served}")

# create another object call User with Values for an user. define the vales
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
    def describe_user(self):
        summary = f"This user full name is {self.first} {self.last} and their ID number is {self.id}."
        print(f"\n{summary}")
    def greet_user(self):
        greet = f"Hello {self.first}, welcome to the company!"
        print(f"\n{greet}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

Emilio = User("emilio", "salazar", "15", "682", "emiliosalaza15@gmail.com", "21")
memo = User("first", "last", "10", "469", "emsalazarppca1211@gmail.com", "22")


print()
# call function to greet user and to describe them.
Emilio.greet_user()
Emilio.describe_user()

# call function to imitate a login attempt 
Emilio.increment_login_attempts()
Emilio.increment_login_attempts()
Emilio.increment_login_attempts()
Emilio.increment_login_attempts()
memo.increment_login_attempts()
memo.increment_login_attempts()
memo.increment_login_attempts()


# show the number of login attempts from Emilio and reset attempts
print(f"number of login attempts: {Emilio.login_attempts}")

Emilio.reset_login_attempts()
print(f"Emilio reset of login attempts: {Emilio.login_attempts}")

# show the number of login attempts from memo and reset attempts

print(f" MEMO login attempts: {memo.login_attempts}")
memo.reset_login_attempts()
print(f" MEMO reset login attempts: {memo.login_attempts}")

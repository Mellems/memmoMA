# make a class called Restraurant.
class Restaurant():

    def __init__(self, name, cuisine_type):
        # stores two attributes
        self.name = name
        self.cuisine_type = cuisine_type
    #create method. defines function to print out two pieces of information
    def describe_restaurant(self):
        msg = f"{self.name} is awesome and has {self.cuisine_type}."
        print(f"\n{msg}")
    #create another method. print msg that the restaurant is open.
    def open_restaurant(self):
        msg = f"{self.name} is NOW OPEN!!" 
        print(f"\n{msg}")


#create an instance called restaurant from the class.
restaurant = Restaurant("basic", "outline")
memo = Restaurant("morning", "breakfast")
pat = Restaurant("noon", "lunch")
ali = Restaurant("evening", "dinner")
#that prints the two attributes individually
print(restaurant.name)
print(restaurant.cuisine_type)

#call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

memo.describe_restaurant()
pat.describe_restaurant()
ali.describe_restaurant()


#create a new class called User.
class User():
    def __init__(self, first_name, last_name, ID_number, phone_number, email_address, user_age):
    #stores two attributes first_name and last_name
        self.first = first_name.title()
        self.last = last_name
    #create several more attributes taht a user may have: ID_number, phone_number, email_address
        self.id = ID_number
        self.phone = phone_number
        self.email = email_address
        self.age = user_age
    def describe_user(self):
    #method called describe_user() that prints summary of the user's information.
        summary = f"This user full name is {self.first} {self.last} and their ID number is {self.id}."
        print(f"\n{summary}")
    def greet_user(self):
    #method called greet_user() that prints a personalized greeting to the user.
        greet = f"Hello {self.first}, welcome to the company!"
        print(f"\n{greet}")
#creates instances to use
Emilio = User("emilio", "salazar", "15", "682", "emiliosalaza15@gmail.com", "21")
#call methods
Emilio.describe_user()
Emilio.greet_user()


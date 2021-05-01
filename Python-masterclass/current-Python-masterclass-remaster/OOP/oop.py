class Kettle(object):
    # Class attributes
    power_source = "electricity"

    # Constructor
    def __init__(self, make, price):
        # variables with self are attributes of the instance of the class
        self.make = make
        self.price = price
        self.on = False

    # Methods
    # Mutator - Void Return
    def switch_on(self):
        self.on = True

    def get_price(self):
        return self.price

# First instance of Kettle object
kenwood = Kettle("Kenwood", 8.900)
print(kenwood.make)
print(kenwood.price)


# Changing the value of attributes
kenwood.price = 12.75
print(kenwood.price)

# Second instance of Kettle object
hamilton = Kettle("Hamilton", 14.55)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)  # False
hamilton.switch_on()  # change the attribute on from False to True

# ***Calling a method using the class definition***
Kettle.switch_on(kenwood)
print(kenwood.on)  # True

print("*" * 80)

# Adding a new attribute to the instance of the class - only to this specific instance of the class (kenwood)
kenwood.power = 1.5
print(kenwood.power)

# print(hamilton.power) attribute power doesn't exist for hamilton

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
# Changing the class variable of instances to local attribute variables of instance
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)


print(Kettle.__dict__)
# Accessing instance specific attributes and their values
print(kenwood.__dict__)
print(hamilton.__dict__)









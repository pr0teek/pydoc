my_name = 'Prateek Shukla'
my_age = 26  # not a lie
my_height = 61.32  # inches
my_weight = 70  # kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

height_cm = round(2.54 * my_height)
weight_pounds = round(2.20462 * my_weight)

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} Kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")

print(f"Height in centimeter is {height_cm}.")
print(f"Weight in pounds is {weight_pounds}.")

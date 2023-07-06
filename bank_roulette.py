# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
random_name = random.randint(1, length - 1)
print(f"{names[random_name]} is going to buy the meal today!")
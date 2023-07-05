# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_name = name1 + name2
combine_name_string = combine_name.lower()

t = combine_name_string.count("t")
r = combine_name_string.count("r")
u = combine_name_string.count("u")
e = combine_name_string.count("e")

true = t + r + u + e

l = combine_name_string.count("l")
o = combine_name_string.count("o")
v = combine_name_string.count("v")
e = combine_name_string.count("e")

love = l + o + v + e
total = int(str(true) + str(love))
if (total < 10) or (total > 90):
    print(f"Your score is {total} you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
# String concatenation 
# We want to create a string that says "subscribe to ____"

# Youtuber channel variable
youtuber = ""

# User input
youtuber = input('Enter the name of the youtuber:')

# Different ways to concatenate strings in Python

# 1. concatenate operator
print('Subscribe to ' + youtuber)

# 2. Formatting main string
print("Subscribe to {}".format(youtuber))

# 3. F strings
print(f"Subscribe to {youtuber}")

# Second Example

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

print(f"Computer programming is so {adj}! It makes me so excited all the time because \
      I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}")
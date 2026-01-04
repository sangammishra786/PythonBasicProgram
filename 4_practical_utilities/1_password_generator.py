# Concept: Asks the user for a password length and generates
# a random string of letters, numbers, and symbols.

# Skills: import random, import string, and joining lists into strings.
import random
import string


password_length = int(input("Enter the length of password:- "))
password_list = []

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(0, password_length):
    password_list.append(random.choice(characters))

generated_password = "".join(password_list)
print(f"Final passowrd is:-  {generated_password}")

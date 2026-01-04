# Password generator program (using function)
import random
import string


def generate_password(password):
    if password < 4:
        return None
    password_chars = []

    # Add the mandatory characters in the password
    password_chars.append(random.choice(string.ascii_uppercase))
    password_chars.append(random.choice(string.digits))
    password_chars.append(random.choice(string.punctuation))

    remaining_length = password - 3
    all_characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(remaining_length):
        password_chars.append(random.choice(all_characters))

    # shuffle for randomness
    random.shuffle(password_chars)

    # join the character to generate the password
    return "".join(password_chars)


# check the strength of the password
def check_password_strength(generate_password):
    length = len(generate_password)

    has_upper = any(c.isupper() for c in generate_password)
    has_digit = any(c.isdigit() for c in generate_password)
    has_symbol = any(c in string.punctuation for c in generate_password)

    if length >= 12 and has_upper and has_digit and has_symbol:
        return "🟢 Strong password"
    if length >= 8 and has_upper and has_digit and has_symbol:
        return "🟡 Medium password"
    else:
        return "🔴 Weak"


# Main function
password_length = int(input("Enter the password length:- "))
final_password = generate_password(password_length)

if final_password:
    print(f"Your new generated password is {final_password}")
    print("Your password strength:- ", check_password_strength(final_password))
else:
    print("Password length must be greater than 4")

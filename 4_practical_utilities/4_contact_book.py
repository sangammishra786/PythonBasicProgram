# Concept: Store names and phone numbers. You can search for a name to
# retrieve the number.

# Skills: Dictionaries (Key-Value pairs are perfect for this), input handling.
contact_book = {
    "sangam": "7505350989",
    "devendar": "1234567890",
    "satyam": "7895236410",
    "shivam": "1235638567",
    "mohan": "9654127865",
}


def search_contact_number(name):
    if name in contact_book:
        print(f"Contact Number of {name.title()} is {contact_book[name]}")
    else:
        print(f"{name} is not in the contact book.")


# ===========Main Program================
search_name = input("Enter the name:- ")
search_contact_number(search_name.lower())

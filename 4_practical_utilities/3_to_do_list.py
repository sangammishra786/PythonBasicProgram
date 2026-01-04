# Concept: A program that allows the user to Add, View, and
# Remove tasks from a list.

# Skills: Infinite while loops, list methods (.append(), .remove(), .pop()).
book_list = []


def add_book():
    book_name = input("Enter the book name:- ")
    book_list.append(book_name.lower())


def show_book_list():
    for k, v in enumerate(book_list):
        print(k, v)


def remove_book(book_name):
    if book_name in book_list:
        # this will remove top item of list
        # book_list.pop()
        book_list.remove(book_name)
    else:
        print(f"{book_name} is not in present")


# ==============Main Program ================
is_true = True
while is_true:
    print(
        """
1. Add book
2. View book List
3. Remove book
4. Exit
"""
    )

    user_choice = int(input("Enter the choice:- "))
    if user_choice == 1:
        add_book()
    elif user_choice == 2:
        show_book_list()
    elif user_choice == 3:
        book_name = input("Enter the book to be remove:- ")
        remove_book(book_name.lower())
    elif user_choice == 4:
        is_true = False
        break
    else:
        print("Wrong choice, try again !!")

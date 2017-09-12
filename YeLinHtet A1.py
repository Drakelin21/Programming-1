__author__ = 'Ye Lin Htet'
"""
CP1404 SP52 Programming 1 - Assignment 1
    Name : Ye Lin Htet
    ID : 13258895
    Github : https://github.com/Drakelin21/Programming-1

    Pseudocode:

    function main:
    print (Reading List 1.0 - by Ye Lin Htet)
    in_file = open
        a variable created for opening csv file
    menu_choice = menu()
        a variable used for calling menu function
    if menu_choice == "R"
        function for required books is called
    if menu_choice == "C"
        function for completed books is called
    if menu choice == "A"
        function for adding new books is called
    if menu choice == "M"
        function for marking books is called
    if menu choice == "Q"
        function for quitting the main is called

"""
import csv

def main():
    print("Reading List 1.0 - by Ye Lin Htet")
    in_file = open("books.csv", "r")
    reader = csv.reader(in_file)
    book_list = sorted(reader)
    print(book_list)
    keep_going = "Y"
    menu_choice = menu()
    while keep_going == "Y":
        if menu_choice == "R":
            required_books(book_list)
            menu_choice = menu()
        elif menu_choice == "C":
            completed_books(book_list)
            menu_choice = menu()
        elif menu_choice == "A":
            add_new_book(book_list)
            menu_choice = menu()
        elif menu_choice == "M":
            #mark_complete_books()
            menu_choice = menu()
        else:
            print("Have a nice day :)")
            keep_going = "N"


def menu():
    print("R - List Required Books", "C - List Completed Books", "A - Add new Book",
          "M - Mark Book as Completed", "Q - Quit", sep='\n')
    menu_input = input(">>>: ").upper()
    while menu_input != "R" and menu_input != "C" and menu_input != "A" and menu_input != "M" and menu_input != "Q":
        menu_input = input("Please Enter a Valid Choice")
    return menu_input

def required_books(book_list):
    list_count = 0
    for row in book_list:
        if row[3] == "r":
            list_count += 1
            print("{}{}".format(list_count,row))

def completed_books(book_list):
    for row in book_list:
        if row[3] == "c":
            print("{}".format(row))


def add_new_book(book_list):
    new_book = []
    book_title = input("Enter title of book:")
    while book_title == "":
        book_title = input("Please enter title:")
    new_book.append(book_title)
    book_author = input("Enter book Author:")
    while book_author == "":
        book_author = input("Please enter author:")
    new_book.append(book_author)
    valid_number = False
    while not valid_number:
        try:
            page_numbers = int(input("How many pages:"))
            while page_numbers <= 0:
                page_numbers = int(input("Enter a number above 0"))
            valid_number = True
        except ValueError:
            print("Please Enter valid number")
    new_book.append(page_numbers)
    new_book.append("r")
    book_list.append(new_book)
    return book_list


main()
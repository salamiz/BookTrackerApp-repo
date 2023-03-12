# Author:         Zulkifli Salami
# Program:        book_tracker_app
# Date Created:   02-09-23
# Date Modified:  02-10-23
# Description: A program that can store and retrieve information related to a user's reading list.
# User's would be able to add a book to the list using functions, program stores information about all the books in a csv file,
# user's will be able to retrieve the books using functions from the reading list, and user's will be able to search for books.

import csv

# function to add a book to the reading list
def add_book():
    need_input = True
    while need_input:
        # get book title
        title = input("Enter book title: ").strip()
        # validate title
        if not title:
            print("Title cannot be empty or contain only spaces.")
            need_input = True
        else:
            break


    need_input1 = True
    while need_input1:
        # get author name
        author = input("Enter author name: ").strip()
        # validate author name
        if not author:
            print("Author name cannot be empty or contain only spaces.")
            need_input1 = True
        # check if title contains only digits
        elif author.isdigit():
            print("Author can not be numbers only.")
            need_input1 = True
        else:
            break
    
    need_input2 = True
    while need_input2:
        # get year of publication
        year = input("Enter year of publication: ").strip()
        # validate year
        if not year.isdigit() or int(year) <= 0:
            print("Year must be a positive numeric value greater than zero.")
            need_input2 = True
        # break loop if all inputs are valid
        else:
            need_input2 = False
    
    # write to csv file
    with open('books.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title, author, year])
    # confirmation message
    print("Book added successfully!")

# function to retrieve all books in the reading list
def retrieve_books():
    with open("books.csv", "r") as file:
        # Use csv.reader to read the contents of the books.csv file
        reader = csv.reader(file)
        # Convert the reader object to a list of lists
        books = list(reader)
        # Check if the list is not empty
        if not books:
            # If the list is empty, print a message and return
            print("No books in the reading list.")
            return
        # Iterate through the list of books
        for book in books:
            # Print each book in the format: "- Title by Author (Year)"
            print(f"- {book[0]} by {book[1]} ({book[2]})")

# function to search for a book in the reading list
def search_book():
    # get title to search
    while True:
        title = input("Enter book title to search: ").strip()
        # validate title
        if not title:
            print("Title cannot be empty or contain only spaces.")
            continue
        # break loop if title is valid
        break
    # list to store books
    books = []
    
    # read from csv file
    with open('books.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            books.append(row)
    
    # search for book
    found = False
    for book in books:
        if book[0].lower() == title.lower():
            print(f"Book found: {book[0]} by {book[1]} ({book[2]})")
            found = True
            break
    
    if not found:
        print(f"Book with title '{title}' not found.")
  
def main():
    while True:
        print("""
        Reading List Menu:
        1. Add a book
        2. List all books
        3. Search for a book
        4. Quit
        """)
        
        option = input("Enter option number: ").strip()
        if not option.isdigit() or int(option) < 1 or int(option) > 4:
            print("Invalid option. Please enter a valid option number.")
            continue
        
        if option == '1':
            add_book()
        elif option == '2':
            retrieve_books()
        elif option == '3':
            search_book()
        elif option == '4':
            break
    
    print("Goodbye!")


# Check function to be called 
if __name__ == '__main__':
    # If main() run program
    main()


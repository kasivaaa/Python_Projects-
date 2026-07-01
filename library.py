library = {
    "Python basics": "Available",
    "Data science": "Borrowed",
    "Web Development": "Available",
    "Machine learning": "Available",
}

#function to display the books
def display_books():
    print("Available books in the library:")
    for book, status in library.items():
        if status == "Available":
            print(f"{book} - {status}")

#function to borrow a book
def borrow_book(book_name):
    if book_name in library:
        if library[book_name] == "Available":
            library[book_name] = "Borrowed"
            print(f"You have borrowed {book_name}.")
        else:
            print(f"Sorry, {book_name} is already borrowed.")
    else:
        print(f"Book '{book_name}' not found in the library.")

#function to return a book
def return_book(book_name):
    if book_name in library:
        if library[book_name] == "Borrowed":
            library[book_name] = "Available"
            print(f"You have returned {book_name}.")
        else:
            print(f"{book_name} was not borrowed.")
    else:
        print(f"Book '{book_name}' not found in the library.")
        

#main program
while True:
    print("\n ----------Library books----------")
    print ("1. Display available books")
    print ("2. Borrow a book")
    print ("3. Return a book")
    print ("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        display_books()
    elif choice == "2":
        book = input("Enter the name of the book you want to borrow: ")
        borrow_book(book)

    elif choice == "3":
        book = input("Enter the name of the book you want to return: ")
        return_book(book)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

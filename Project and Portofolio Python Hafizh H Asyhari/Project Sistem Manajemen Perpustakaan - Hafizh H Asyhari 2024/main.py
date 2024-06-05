// Main //
// Author by Hafizh H Asyhari //
// 2024 //

import lib
from Book import Book
library = []
archived_books = []
LMS = []

def lms():
    load_library_data()
    while True:
        print("           *****************          ")
        print("      Library Management System       ")
        print("1. Add a new book")
        print("2. Search for books")
        print("3. Edit book information")
        print("4. Archive a book")
        print("5. Remove a book")
        print("6. Generate reports")
        print("7. Exit")
        print("           *****************          ")
        choice = input("Enter your choice : ")
        if choice == "1":
                add_book()
                printLib()
        elif choice == "2":
                search_book()
        elif choice == "3":
                edit_book()
        elif choice == "4":
                archive_book()
        elif choice == "5":
                remove_book()
        elif choice == "6":
                generate_report()
        elif choice == "7":
                file1 = open("LMS.txt","w")
                file2 = open("LIB.txt","w")
                file3 = open("Archive.txt","w")
                lib.print_search_result_infile(LMS, file1)
                lib.print_search_result_infile(library, file2)
                lib.print_search_result_infile(archived_books, file3)
                print("Exiting the Library Management System ")
                exit()
        else:
                print("Invalid Option.please choose number 1-7")
                continue
def book(list,filename):
    try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                book_info = {}
                option = {}
                count_books = 0
                for line in lines:
                    line = line.strip()
                    if line:
                        Item ,value = line.split(" : ")
                        book_info[Item.rstrip("[]$#?;,. %!()/\t").lstrip()] = value.strip("[]$#?;,. %!()/\t")
                    if line == "" and book_info:
                        Title = book_info.get("Title")
                        Publisher = book_info.get("Publisher")
                        ISBN_10 = book_info.get("ISBN-10")
                        ISBN_13 = book_info.get("ISBN-13")
                        if Title and Publisher and ISBN_10 and ISBN_13:
                            for f in book_info:
                                if f not in ["Title","Publisher" ,"ISBN-10","ISBN-13"]:
                                    option[f] = book_info[f]
                            ex_book = find_book_by_isbn(list,ISBN_10, ISBN_13)
                            if ex_book:
                                print("A book "+Title+" already exists in the library .")
                                c = input("Do you want to replace the existing book ? ")
                                if c.lower() == "yes":
                                    ex_book.title = Title
                                    ex_book.publisher = Publisher
                                    ex_book.ISBN_10 = ISBN_10
                                    ex_book.ISBN_13 = ISBN_13
                                    ex_book.option = option
                                    ex_book.number_of_copies = int(book_info.get("NUM_of_Copies"))
                                    print("Book replaced.")
                                else:
                                    ex_book.NUM_of_copies = int(ex_book.NUM_of_copies) + 1
                                    count_books += 1
                                    print("Additional copy of the book "+Title+" added.")
                            else:
                                new_book = Book(Title, Publisher, ISBN_10, ISBN_13,option,"1")
                                list.append(new_book)
                                count_books += 1
                        else:
                            print("Invalid book information, required fields [Title, Publisher, ISBN-10, ISBN-13] not provided.")
                        book_info = {}
                        option = {}
            if count_books == 0:
                print("No books added from the file.")
            return list
    except FileNotFoundError:
        print("File not found ")

def find_book_by_isbn(list,isbn10, isbn13):
    for book in list:
        if book.ISBN_10 == isbn10 or book.ISBN_13 == isbn13:
            return book
    return None
def add_book():
    filename = input("Enter the name of the file including the book information (or press Enter to exit): ")
    while filename:
        book(library, filename)
        book(LMS,filename)
        filename = input("Enter the name of the file including the book information (or press Enter to exit): ")

def printLib():
    i=1
    for book in LMS:
        print(f"Book ({i})")
        lib.print_book_information(book)
        print()
        i+=1
def search_book():
  if len(LMS) == 0:
        print("No Book in library ")
  else:
    while True:
        print("Search Options:")
        attributes = set()
        for book in LMS:
            book_attributes = vars(book)
            attributes.update(book_attributes.keys())
        attributes = sorted(attributes)
        for i, attribute in enumerate(attributes, 1):
            if attribute == "option":
                book_options = set()
                for book in LMS:
                    book_attributes = vars(book)
                    if attribute in book_attributes:
                        options = book_attributes[attribute]
                        book_options.update(options.keys())
                book_options = sorted(book_options)
                print(f"{i}. Search by {attribute} ")
                for j, option in enumerate(book_options, 1):
                    print(f"  {i}.{j}. Search by {option}")
            else:
                print(f"{i}. Search by {attribute}")
        print(f"{len(attributes) + 1}. Return to menu ")
        ch = input("Enter your choice: ")
        if int(ch) == (len(attributes) + 1):
             break
        elif ch.isdigit() and 1 <= int(ch) <= len(attributes):
            attribute = attributes[int(ch) - 1]
            if attribute == "option":
                option_ch = input("Enter your choice for Options: ")
                if option_ch.isdigit() and 1 <= int(option_ch) <= len(book_options):
                    option_attribute = book_options[int(option_ch) - 1]
                    search_value = input("Enter the search item: ")
                    lib.search1(option_attribute, search_value, LMS)
                else:
                    print("Invalid choice for Options. Please try again.")
            else:
                search_value = input("Enter the search item: ")
                lib.search1(attribute, search_value, LMS)
        else:
            print("Invalid choice. Please try again.")

def edit_book():
  if len(LMS) == 0:
        print("No Book in library ")
  else:
    print("Edit Options:")
    print("1. Edit by ISBN number")
    print("2. Edit by file name")
    edit_option = input("Enter your choice: ")
    if edit_option == "1":
        isbn = input("Enter the ISBN number: ")
        book_to_edit = find_book_by_isbn2(LMS,isbn)
        if book_to_edit:
            print("Book found:")
            lib.print_book_information(book_to_edit)
            print()
           ## confirm = input("Do you want to edit this book? (yes/no): ")
           #// if confirm.lower() == "yes":
            edit_book_attributes(book_to_edit)
          # // else:
             #   print("Edit operation cancelled.")
        else:
            print("Book not found.")
    elif edit_option == "2":
        filename = input("Enter the name of the file: ")
        books_to_edit = find_books_by_file(filename)
        if len(books_to_edit) == 0:
            print("No books found in the file.")
            return
        for book_to_edit in books_to_edit:
            print("Book found:")
            lib.print_book_information(book_to_edit)
            print()
            confirm = input("Do you want to edit this book? (yes/no): ")
            if confirm.lower() == "yes":
                edit_book_attributes(book_to_edit)
            else:
                print("Edit operation cancelled.")
    else:
        print("Invalid edit option.")

def find_books_by_file(filename):
    found_books = []
    book(found_books,filename)
    return found_books
def find_book_by_isbn2(list,isbn):
    for book in list:
        if book.ISBN_10 == isbn or book.ISBN_13 == isbn:
            return book
    return None

def edit_book_attributes(book):
    confirm_changes = input("Do you want to edit this book? (yes/no): ")
    if confirm_changes.lower() == "yes":
        # Store the original values of book attributes
        original_title = book.Title
        original_publisher = book.Publisher
        original_option = dict(book.option)
        original_copy = book.NUM_of_copies
        new_title = input("Enter the new title (press enter to keep the current value): ")
        new_publisher = input("Enter the new publisher (press enter to keep the current value): ")
        NumCopy = input("Enter the new number of copies (press enter to keep the current value): ")
        if new_title:
            book.Title = new_title
        if new_publisher:
            book.Publisher = new_publisher
        if NumCopy:
            book.NUM_of_copies= NumCopy
        print("Current Options:")
        option = book.option
        option_keys = list(option.keys())
        for i, key in enumerate(option_keys, 1):
            print(f"{i}. {key}: {option[key]}")

        while True:
            option_choice = input("Enter the option number to edit (press enter to exit): ")
            if not option_choice:
                break
            elif option_choice.isdigit() and 1 <= int(option_choice) <= len(option_keys):
                selected_key = option_keys[int(option_choice) - 1]
                new_value = input(f"Enter the new value for {selected_key} (press enter to keep the current value): ")
                if new_value:
                    option[selected_key] = new_value
                else:
                    del option[selected_key]
                print("Option updated.")
            else:
                print("Invalid option number. Please try again.")

        print("Book information updated.")
        confirm_edit_list = input("Do you want to update the book in the library, archived books, and LMS? (yes/no): ")

        if confirm_edit_list.lower() == "yes":
            # Update the book in all required lists
            if book in library:
                update_book_in_list(book, library)
            if book in archived_books:
                update_book_in_list(book, archived_books)
            if book in LMS:
                update_book_in_list(book, LMS)

            print("Book updated in the library, archived books, and LMS.")
        else:
            confirm_cancel = input("Are you sure you want to cancel all previous changes? (yes/no): ")
            if confirm_cancel.lower() == "yes":
                # Revert changes made to the book
                book.Title = original_title
                book.Publisher = original_publisher
                book.option = original_option
                book.NUM_of_copies=original_copy
                print("Update operation cancelled. All previous changes to this book reverted.")
            else:
                print("Update operation cancelled. Previous changes to this book still apply.")
    else:
        print("Edit operation cancelled. No changes made.")


def update_book_in_list(book, book_list):
    for b in book_list:
        if b.ISBN_10 == book.ISBN_10 or b.ISBN_13 == book.ISBN_13:
            b.Title = book.Title
            b.Publisher = book.Publisher
            b.option = book.option
            b.NUM_of_copies = book.NUM_of_copies

    print("Book updated in the list.")

def archive_book():
  if len(LMS) == 0:
        print("No Book in library ")
  else:
    isbn = input("Enter the ISBN of the book(s) you want to archive (separated by commas if multiple): ")
    isbn_list = isbn.split(",")

    for isbn in isbn_list:
        book_to_archive = find_book_by_isbn2(LMS, isbn)

        if book_to_archive:
            num_of_copies = int(book_to_archive.NUM_of_copies)

            if num_of_copies == 1:
                print("Only 1 copy of the book is available.")
                confirm_archive = input("Do you want to archive this copy? (yes/no): ")

                if confirm_archive.lower() == "yes":
                    if book_to_archive in library:
                        library.remove(book_to_archive)
                    archived_books.append(book_to_archive)
                    print("Book archived.")
                else:
                    print("Archiving cancelled.")
            else:
                print(f"Number of copies available for ISBN {isbn}: {num_of_copies}")
                copies_to_archive = int(input("Enter the number of copies you want to archive: "))

                if copies_to_archive > num_of_copies:
                    print("Invalid number of copies. Archiving cancelled.")
                else:
                    book_to_archive.NUM_of_copies = str(num_of_copies - copies_to_archive)

                    if book_to_archive.NUM_of_copies == "0":
                        if book_to_archive in library:
                            library.remove(book_to_archive)
                        book_to_archive.NUM_of_copies = str(copies_to_archive)
                        archived_books.append(book_to_archive)
                    else:
                        book_to_archive.NUM_of_copies = str(copies_to_archive)
                        archived_books.append(book_to_archive)
                        book_to_archive.NUM_of_copies = str(num_of_copies - copies_to_archive)

                    print(f"{copies_to_archive} copy/copies of the book with ISBN {isbn} archived.")
        else:
            print(f"No book found with the ISBN {isbn}. Archiving cancelled.")

    print("Archived books:")
    for book in archived_books:
        print(book.Title)


def remove_book():
    if len(LMS) == 0:
        print("No books in the LMS.")
        return

    isbn = input("Enter the ISBN of the book you want to remove: ")
    book_to_remove = find_book_by_isbn2(archived_books, isbn)

    if book_to_remove:
        print("Book found in the archived books:")
        lib.print_book_information(book_to_remove)
        print()
        confirm = input("Are you sure you want to remove this book from the archived books and the LMS? (yes/no): ")
        if confirm.lower() == "yes":
            if book_to_remove in archived_books:
                archived_books.remove(book_to_remove)
            if book_to_remove in LMS:
                LMS.remove(book_to_remove)
            print("Book removed from the archived books and the LMS.")
        else:
            print("Removal operation cancelled.")
    else:
        print("Book not found in the archived books.")

def generate_report():
  if len(LMS) == 0:
        print("No Book in library ")
  else:
    print(" Generating LMS Reports")
    books = 0
    for book in LMS:
        books += int(book.NUM_of_copies)
    print("--> Total number of books in the LMS:", books)

    different_books = len(LMS)
    print("--> Number of different books in the LMS :", different_books)

    archived_count = 0
    for book in archived_books:
        archived_count += int(book.NUM_of_copies)
    print("--> Number of books archived in the LMS:",archived_count)
    y = input("Enter the year to find the number of books that were released after this year: ")
    newer_books = 0
    for book9 in LMS:
        if book9.option is not None and "Year" in book9.option and int(book9.option["Year"]) > int(y):
            newer_books += int(book9.NUM_of_copies)
    print("--> Number of books newer than", y, "in the LMS:", newer_books)

    pub_distribution = {}
    for book3 in LMS:
        publisher = book3.Publisher
        if publisher in pub_distribution:
            pub_distribution[publisher].append(book3.Title)
        else:
            pub_distribution[publisher] = [book3.Title]
    print("--> Book distribution by publisher:")
    k=1
    for publisher, titles in pub_distribution.items():
        print(f" {k}- Publisher: {publisher}")
        I=1
        for title in titles:
            print(f"     {I}. {title}")
            I+=1
        k+=1

    y_distribution = {}
    for book1 in LMS:
        if book1.option is not None and "Year" in book1.option:
            y1 = book1.option["Year"]
            if y1 in y_distribution:
                y_distribution[y1].append(book1.Title)
            else:
                y_distribution[y1] = [book1.Title]
    print("--> Book distribution by year:")
    k = 1
    for year, titles in y_distribution.items():
        print(f" {k}- Year: {year}")
        I = 1
        for title in titles:
            print(f"     {I}. {title}")
            I += 1
        k += 1

def load_library_data():
    try:
        with open("LMS.txt", "r") as file:
           load(LMS,file)
    except FileNotFoundError:
        return []
    try:
        with open("LIB.txt", "r") as file1:
           load(library,file1)
    except FileNotFoundError:
        return []
    try:
        with open("Archive.txt", "r") as file2:
           load(archived_books,file2)
    except FileNotFoundError:
        return []
def load_library_data():
    try:
        with open("LMS.txt", "r") as file:
           load(LMS,file)
    except FileNotFoundError:
        return []
    try:
        with open("LIB.txt", "r") as file1:
           load(library,file1)
    except FileNotFoundError:
        return []
    try:
        with open("Archive.txt", "r") as file2:
           load(archived_books,file2)
    except FileNotFoundError:
        return []

def load(list,file):
            lines = file.readlines()
            book_info = {}
            option={}
            for line in lines:
                line = line.strip()
                if line:
                    key, value = line.split(" : ")
                    book_info[key] = value
                if line == "" and book_info:
                    for f in book_info:
                        if f not in ["Title","Publisher","ISBN-10","ISBN-13","NUM_of_Copies"]:
                            option[f] = book_info[f]
                    new_book = Book(
                        book_info.get("Title"),
                        book_info.get("Publisher"),
                        book_info.get("ISBN-10"),
                        book_info.get("ISBN-13"),
                        option,
                        book_info.get("NUM_of_Copies")
                    )
                    list.append(new_book)
                    option={}
                    book_info = {}


// Proyek Sistem Manajemen Perpustakaan //
// Author by Hafizh H Asyhari @hafizhhasyhari //
// Date : 2024 //

lms()

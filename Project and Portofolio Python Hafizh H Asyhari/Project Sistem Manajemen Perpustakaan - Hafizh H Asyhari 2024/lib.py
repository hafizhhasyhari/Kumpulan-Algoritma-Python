
def print_book_information(book):
        print(f"Title : {book.Title}")
        print(f"Publisher : {book.Publisher}")
        print(f"ISBN-10 : {book.ISBN_10}")
        print(f"ISBN-13 : {book.ISBN_13}")
        for b in book.option :
          print(f"{b} : {book.option[b]}")
        print(f"NUM_of_Copies : {book.NUM_of_copies}")

def print_search_result_infile(res, file):
    for book in res:
         file.write(f"Title : {book.Title}\n")
         file.write(f"Publisher : {book.Publisher}\n")
         file.write(f"ISBN-10 : {book.ISBN_10}\n")
         file.write(f"ISBN-13 : {book.ISBN_13}\n")
         for b in book.option:
            file.write(f"{b} : {book.option[b]}\n")
         file.write(f"NUM_of_Copies : {book.NUM_of_copies}\n")
         file.write("\n")

def search1(att, value, library):
    res = []
    if att not in ["Title", "Publisher", "ISBN_10", "ISBN_13", "NUM_of_copies"]:
         for book in library :
            book_attributes = book.option
            if att in book_attributes:
              options = book_attributes[att]
              if value == options :
                 res.append(book)
    else:
        for book in library:
            if getattr(book, att, "") == value:
                res.append(book)

    if res:
        for book in res:
            print_book_information(book)
            print()
        x = input("Do you want to store the result in a file? ")
        if x.lower() == "yes":
            fname = input("Enter file name: ")
            file1 = open(fname, 'w')
            print_search_result_infile(res, file1)
            print("Search results stored in the file:", fname)
            file1.close()
    else:
        print("No books found with the given " + att)

// Lib program //
// Author by Hafizh H Asyhari @hafizhhasyhari
// Date : 2024 //

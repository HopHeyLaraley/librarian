from librarian import Book, Librarian

def menu():
    librarian = Librarian()
    while True:
        print("\nSelect action : \n1.Books list\n2.Set book\n3.Delete book\n4.Change status\n5.Find book\n0.Exit")
        try:
            action = int(input())
            if action == 1:
                librarian.show_books()
            elif action == 2:
                book = Book()
                librarian.set_book(book)
            elif action == 3:
                id = int(input('Write ID : '))
                librarian.remove_book(id)
            elif action == 4:
                id = int(input('Write ID : '))
                librarian.update_book(id)
            elif action == 5:
                librarian.find_book()
            elif action == 0:
                break
            else:
                print("Choose valid option\n")
        except ValueError:
            print("Invalid input. Enter a number\n")

menu()

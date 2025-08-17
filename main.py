import database

def main_menu():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Delete Member")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            database.add_book(title, author, price, quantity)
            print("Book added successfully!")

        elif choice == "2":
            books = database.view_books()
            print("\n--- Books ---")
            for b in books:
                print(b)

        elif choice == "3":
            book_id = int(input("Book ID to update: "))
            price = float(input("New Price: "))
            quantity = int(input("New Quantity: "))
            database.update_book(book_id, price, quantity)
            print("Book updated successfully!")

        elif choice == "4":
            book_id = int(input("Book ID to delete: "))
            database.delete_book(book_id)
            print("Book deleted successfully!")

        elif choice == "5":
            name = input("Name: ")
            email = input("Email: ")
            database.add_member(name, email)
            print("Member added successfully!")

        elif choice == "6":
            members = database.view_members()
            print("\n--- Members ---")
            for m in members:
                print(m)

        elif choice == "7":
            member_id = int(input("Member ID to delete: "))
            database.delete_member(member_id)
            print("Member deleted successfully!")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()

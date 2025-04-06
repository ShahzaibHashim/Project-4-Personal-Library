import json
import os

# File to store library data
data_file = 'library.txt'

# Load library from file
def load_library():
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    print("\nAdd a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")

    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read = read_input == "yes"

    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    print("\nRemove a Book")
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]

    if len(library) < initial_length:
        print("Book removed successfully!")
    else:
        print("Book not found!")

# Search for a book
def search_library(library):
    print("\nSearch for a Book")
    print("Search by: ")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == '1':
        search_by = 'title'
    elif choice == '2':
        search_by = 'author'
    else:
        print("Invalid choice!")
        return

    search_term = input(f"Enter the {search_by}: ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    print("\nDisplay All Books")
    if not library:
        print("Library is empty.")
        return

    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_statistics(library):
    print("\nDisplay Statistics")
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return

    read_count = sum(1 for book in library if book['read'])
    percent_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main menu
def main():
    library = load_library()
    print("Welcome to your Personal Library Manager!")

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

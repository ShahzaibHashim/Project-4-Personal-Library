import streamlit as st
import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library, title, author, year, genre, read):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    save_library(library)
    st.success("Book added successfully!")

def remove_book(library, title):
    original_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < original_length:
        save_library(library)
        st.success("Book removed successfully!")
    else:
        st.warning("Book not found.")

def search_books(library, keyword):
    return [book for book in library if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]

def display_books(library):
    for book in library:
        st.markdown(f"**Title:** {book['title']}")
        st.markdown(f"Author: {book['author']}")
        st.markdown(f"Year: {book['year']}")
        st.markdown(f"Genre: {book['genre']}")
        st.markdown(f"Read: {'Yes' if book['read'] else 'No'}")
        st.markdown("---")

def library_statistics(library):
    total_books = len(library)
    read_books = sum(book['read'] for book in library)
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    return total_books, read_books, unread_books, read_percentage

# Load library
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")

menu = st.sidebar.selectbox("Choose an option", [
    "Add Book", "Remove Book", "Search Book", "Display All Books", "Library Statistics"
])

if menu == "Add Book":
    st.header("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read it?")

    if st.button("Add Book"):
        if title and author and genre:
            add_book(library, title, author, year, genre, read)
        else:
            st.warning("Please fill all the fields.")

elif menu == "Remove Book":
    st.header("❌ Remove a Book")
    title = st.text_input("Enter title to remove")
    if st.button("Remove"):
        if title:
            remove_book(library, title)
        else:
            st.warning("Please enter a title.")

elif menu == "Search Book":
    st.header("🔍 Search for a Book")
    keyword = st.text_input("Enter keyword (title/author)")
    if keyword:
        results = search_books(library, keyword)
        if results:
            st.success(f"Found {len(results)} result(s):")
            display_books(results)
        else:
            st.info("No matching books found.")

elif menu == "Display All Books":
    st.header("📖 All Books in Your Library")
    if library:
        display_books(library)
    else:
        st.info("Library is empty.")

elif menu == "Library Statistics":
    st.header("📊 Library Statistics")
    total, read, unread, percent = library_statistics(library)
    st.write(f"**Total Books:** {total}")
    st.write(f"**Books Read:** {read}")
    st.write(f"**Books Unread:** {unread}")
    st.write(f"**Read Percentage:** {percent:.2f}%")

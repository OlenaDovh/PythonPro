import json


def manage_books(file_path: str,
                 new_b_name: str,
                 new_b_author: str,
                 new_b_year: int,
                 new_b_availability: bool) -> None:
    """
    Loads books from a json file, displays available books,
    and adds a new book to the collection
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        books = json.load(file)

    available_books = [book for book in books if book["наявність"] is True]

    for book in available_books:
        print(f"📖 '{book['назва']}' — {book['автор']} ({book['рік']} - наявна)")

    print("\n--- Додавання нової книги ---")
    new_book = {
        "назва": new_b_name,
        "автор": new_b_author,
        "рік": new_b_year,
        "наявність": new_b_availability
    }

    books.append(new_book)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(books, json_file, indent=4)

    print(f"\nКнигу '{new_b_name}' ({new_b_year} р.) автора {new_b_author} успішно додано.")


manage_books("library.json", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", 2014, True)

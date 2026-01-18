import json


def manage_books(filename, new_b_name, new_b_author, new_b_year, new_b_pr):
    with open(filename, 'r', encoding='utf-8') as f:
        books = json.load(f)

    available_books = [b for b in books if b["наявність"] is True]

    for book in available_books:
        print(f"📖 '{book['назва']}' — {book['автор']} ({book['рік']})")

    print("\n--- Додавання нової книги ---")
    new_book = {
        "назва": new_b_name,
        "автор": new_b_author,
        "рік": new_b_year,
        "наявність": new_b_pr
    }

    books.append(new_book)

    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

    print(f"\nКнигу '{new_book['назва']}' успішно додано.")

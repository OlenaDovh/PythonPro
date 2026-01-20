from csv import DictReader, writer


def csv_reader_writer(file_path: str, new_st_name: str, new_st_age: int, new_st_score: int) -> None:
    """
    Reads student data from a csv file, calculates the average score
    and adds a new student if the name is unique
    """
    scores = []
    is_unique = True

    with open(file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            name = row["Ім'я"]
            score = int(row['Оцінка'])
            scores.append(score)
            print(f"Ім'я {name} | Вік {row['Вік']} | Оцінка {score}")

            if new_st_name.strip().lower() == name.strip().lower():
                is_unique = False

    if scores:
        print(f"Середня оцінка: {sum(scores) / len(scores):.2f}")

    if is_unique:
        with open(file_path, "a", newline="", encoding="utf-8") as csv_file2:
            writer(csv_file2).writerow([new_st_name, new_st_age, new_st_score])
            print(f"Студент {new_st_name} успішно доданий.")
    else:
        print(f"Cтудент {new_st_name} вже існує у файлі. "
              f"Додайте іншого студента")


csv_reader_writer("students.csv", "Євген", 20, 95)

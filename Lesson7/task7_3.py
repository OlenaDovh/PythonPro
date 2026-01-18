from csv import DictReader, writer


def csv_reader(filename, new_st_name, new_st_age, new_st_score):
    scores = []
    is_unique = True

    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
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
        with open(filename, "a", newline="", encoding="utf-8") as csv_file2:
            writer(csv_file2).writerow([new_st_name, new_st_age, new_st_score])
            print(f"Студент {new_st_name} успішно доданий.")
    else:
        print(f"Cтудент {new_st_name} вже існує у файлі. Додайте іншого студента")

csv_reader("students.csv", "Євген", 20, 95)

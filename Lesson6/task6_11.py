from typing import Generator


def get_avg(file_path: str) -> Generator:
    """Incrementally computes the average of numerical values from a file"""
    count = 0
    total = 0
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                value = float(line.strip())
                count += 1
                total += value
                yield total / count
            except ValueError:
                pass


for avg in get_avg("Avg.txt"):
    print(f'{avg:.2f}')

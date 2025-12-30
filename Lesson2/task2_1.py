import builtins


def my_sum() -> None:
    """ Overrides built-in function sum()."""

    def sums(nums: int | float | list[int | float]) -> str:
        print(nums)
        return "This is my custom sum function!"

    global sum
    sum = sums


numbers = [1, 15, 23, 47, 3, 89, 13, 1, 16.0]

summa = sum

print(sum(numbers))  # викликається вбудована функція sum()
print(my_sum())  # функція sum() перевизначена при виклику my_sum()
print(sum(numbers))  # викликається локальна функція sum()
print(builtins.sum(numbers))  # викликається вбудована функція sum() з модуля builtins
print(summa(numbers))  # викликається вбудована функція sum(), посилання на яке збережено в змінній summa

import codecs


class EmptyFileError(Exception):
    """Defines a custom exception raised when an input file is empty"""


def arithmetic_mean(file):
    try:
        with codecs.open(file, 'r', 'utf-8') as work_file:
            read_file = work_file.read().strip()

        if not read_file:
            raise EmptyFileError("File is empty")

        content = read_file.split()
        nums = []
        for char in content:
            nums.append(float(char))

        return sum(nums) / len(nums)

    except FileNotFoundError:
        print("The file was not found in the target directory")
    except EmptyFileError as e:
        print(e)
    except ValueError as e:
        print("The file contains non-numerical data")
    except Exception as e:
        print(f"Unknown error: {e}")


arithmetic_mean('Test.txt')
arithmetic_mean('empty.txt')
arithmetic_mean('non_numerical_values.txt')
assert arithmetic_mean('nums_in_one_row.txt') == 5.5
assert arithmetic_mean('nums_in_one_column.txt') == 5.5
assert arithmetic_mean('nums_in_row_and_column.txt') == 5.5
assert arithmetic_mean('float_values.txt') == 2.5
assert arithmetic_mean('negative_nums.txt') == 3.75

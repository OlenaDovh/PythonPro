import os
from typing import Generator


def error_log_generator(file_path: str) -> Generator:
    """
    Generator that reads a log file line by line and yields
    only lines containing HTTP error codes (4XX or 5XX)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.isdigit() and len(word) == 3:
                    if word.startswith(('4', '5')):
                        yield line.strip()
                        break


def get_errors_from_logs(input_logs: str, output_logs: str) -> None:
    """
    Extracts error lines from a log file and save them to a new file
    """
    errors_count = 0
    log_gen = error_log_generator(input_logs)

    with open(output_logs, 'w', encoding='utf-8') as out_file:
        for error_line in log_gen:
            out_file.write(error_line + '\n')
            errors_count += 1

    print(f"Processing finished. Rows with errors count: {errors_count}")
    print(f"Results are saved in '{output_logs}'")


get_errors_from_logs("large_server.log", "critical_errors.log")

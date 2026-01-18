from typing import Generator


def get_keyword_line_gen(file_path: str, keyword: str) -> Generator:
    """Generates lines from a file that contain a given keyword"""
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        for line in f:
            if keyword.lower() in line.lower():
                yield line.strip()


def analyze_logs(input_file: str, output_file: str, keyword: str) -> None:
    """
    Analyzes a log file, filter lines containing a keyword,
    and write the results to an output file
    """

    log_gen = get_keyword_line_gen(input_file, keyword)

    count = 0
    with open(output_file, 'w', encoding='utf-8') as out:
        for matched_line in log_gen:
            out.write(matched_line + '\n')
            count += 1
            print(f"Found: '{matched_line}'")

    print(f"Process is finishes. Recorded rows count: {count}")
    print(f"Results are written in : {output_file}")


INPUT_LOG = "LogFileTest.txt"
OUTPUT_RES = "filtered_file_by_keyword.txt"
SEARCH = "ERROR"

analyze_logs(INPUT_LOG, OUTPUT_RES, SEARCH)

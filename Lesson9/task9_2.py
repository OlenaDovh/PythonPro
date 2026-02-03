import re


def get_phone_numbers(text: str) -> list[str]:
    """Searches and returns phone numbers which match pattern"""
    pattern = (r"(?<!\d)(\(\d{3}\)\s\d{3}\-\d{4}|"
               r"\d{3}\.\d{3}\.\d{4}|"
               r"\d{3}\-\d{3}\-\d{4}|"
               r"\d{10})(?!\w+)")
    return re.findall(pattern, text)


new_text = """
If the line is busy, try the backup number (123) 456-7890 (valid) or 123-456-7890.
Some employees prefer dot-separated format like 321.654.0987 (valid), while others publish plain digits such as 5556667777 (valid).

Do not accept numbers with letters like 123-ABC-7890 (invalid) or mixed separators like 123-456.7890 (invalid) if your rule forbids mixing.
123-456-78901 (invalid) or 123...456...7890 (invalid) or 123456789 (invalid) or 12345678912 (invalid) or 123-456-78904 (invalid).
Also reject formats with extra symbols: (123)*456-7890 (invalid) or spaces inside blocks like 123 45 67890 (invalid).
End of contact list (123 456-7890 or 123) 456-7890.
"""

exp_res = ['(123) 456-7890', '123-456-7890', '321.654.0987', '5556667777']


def test_get_phone_numbers():
    assert get_phone_numbers(new_text) == exp_res

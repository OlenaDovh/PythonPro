from unittest import TestSuite, TextTestRunner

from Lesson8.test_task8_1 import StringProcessorTestCases as sp_tests


def suite():
    test_cases = TestSuite()
    test_cases.addTest(sp_tests("test_reverse_string_positive"))
    test_cases.addTest(sp_tests("test_reverse_string_type_error"))
    test_cases.addTest(sp_tests("test_capitalize_several_words_starts_lower"))
    return test_cases


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(suite())

from unittest import skip, TestCase
from Lesson8.task8_1 import StringProcessor


class StringProcessorTestCases(TestCase):

    def setUp(self):
        self.sp = StringProcessor()

    def test_reverse_string_positive(self):
        self.assertEqual(self.sp.reverse_string("Hi! 345"), "543 !iH")

    def test_reverse_1_char(self):
        self.assertEqual(self.sp.reverse_string("A"), "A")

    def test_reverse_string_type_error(self):
        with self.assertRaises(TypeError):
            self.sp.reverse_string(123)  # int
        with self.assertRaises(TypeError):
            self.sp.reverse_string(None)

    @skip("'empty str' will be fixed soon")
    def test_reverse_empty_string(self):
        self.assertEqual(self.sp.reverse_string(""), "")

    def test_capitalize_1_word_starts_lower(self):
        self.assertEqual(self.sp.capitalize_string("flowers"), "Flowers")

    def test_capitalize_several_words_starts_lower(self):
        self.assertNotEqual(self.sp.capitalize_string(
            "flowers and blossoms"), "Flowers And Blossoms")

    def test_capitalize_starts_digit(self):
        self.assertEqual(self.sp.capitalize_string("1flower, 2flower"), "1flower, 2flower")

    def test_count_vowel_positive(self):
        self.assertTrue(self.sp.count_vowels("Синевир! What a wonderful sight") == 9)

    def test_count_zero_vowels(self):
        self.assertFalse(self.sp.count_vowels("МРТ*"))

    @skip("тут буде помилка з деталізацією")
    def test_count(self):
        self.assertGreater(self.sp.count_vowels("Interesting"), self.sp.count_vowels("Interested"),
                           "Кількість голосних в першому слові менше за друге!")

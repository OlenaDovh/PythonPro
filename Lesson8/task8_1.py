class StringProcessor:
    """Defines class which operates strings"""

    def reverse_string(self, s: str) -> str:
        """Reterns a reversed string"""
        if not isinstance(s, str):
            raise TypeError("Only strings allowed")
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Returns a string with the first letter capitalized"""
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """Returns count of vowels in a string"""
        vowels = 'aeiouyаеєиіїоуюя'
        vowel_cnt = 0
        for letter in s:
            if letter in vowels:
                vowel_cnt += 1
        return vowel_cnt

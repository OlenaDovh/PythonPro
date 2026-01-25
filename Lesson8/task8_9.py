class AgeVerifier:
    """Defines class for age validation"""

    def is_adult(self, age: int) -> bool:
        """Validates whether person is adult by its age"""
        if age < 0:
            raise ValueError("Invalid age")
        return age >= 18

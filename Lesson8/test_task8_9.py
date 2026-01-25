import pytest

from Lesson8.task8_9 import AgeVerifier


class TestAgeVerifier:
    @pytest.mark.parametrize("age, exp_res",
                             [(0, False),
                              (17, False),
                              (18, True),
                              (25, True)])
    def test_is_adult_normal(self, age, exp_res):
        assert AgeVerifier().is_adult(age) == exp_res

    @pytest.mark.skip(reason="Некоректний вік менше 0")
    def test_is_adult_negative_age(self):
        AgeVerifier().is_adult(-5)

    @pytest.mark.parametrize("age", [100, 121, 150])
    def test_is_adult_unlikely_scenario(self, age):
        if age > 120:
            pytest.skip(f"Неправильне значення віку '{age}'")
        assert AgeVerifier().is_adult(age) == True

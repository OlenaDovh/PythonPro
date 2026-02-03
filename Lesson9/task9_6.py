import re
import pytest


def validate_password(password: str) -> bool:
    """Validates whether password is strong (meets exact rules)"""
    pattern = (r"^(?=.*[A-Z])"
               r"(?=.*[a-z])"
               r"(?=.*\d)"
               r"(?=.*[!@#$_\-%\^&*(){}\[\]=+])"
               r"(?=\S{8,}$).*$")
    return bool(re.fullmatch(pattern, password))


valid_passwords = ["Abc123@!",
                   "StrongP@ss1",
                   "qWerty9$",
                   "HelloWorld1!",
                   "MyP@ssw0rd",
                   "!Scure#2024",
                   "4Aa1@aaa",
                   "aW12233*21221412"]

invalid_passwords = ["password",
                     "PASSWORD1@",
                     "Passw0rd",
                     "Abcdefg@",
                     "Abc12345",
                     "Ab1@",
                     "12345678@",
                     "abcdefg1@",
                     "124324125124",
                     "!@#$%^&*()_+",
                     "48dw SWd8@"]


@pytest.mark.parametrize("password", valid_passwords)
def test_validate_password_positive(password):
    assert validate_password(password) is True


@pytest.mark.parametrize("password", invalid_passwords)
def test_validate_password_negative(password):
    assert validate_password(password) is False

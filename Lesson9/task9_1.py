import re
import pytest


def is_email_valid(email_addr: str) -> bool:
    """Validates email address using pattern"""
    valid_email_pattern = r"^(?!\.)[a-zA-Z0-9.]+(?<!\.)@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    return bool(re.fullmatch(valid_email_pattern, email_addr))


valid_email_lst = ['user@domain.com',
                   'user1@domain.net',
                   'user.name@domain.org',
                   'a@d.io',
                   'abc.def@domain.co',
                   'user123@domain.info',
                   'name.surname@domain.store',
                   'test1.test2@abc123.dev',
                   'abc@xyz123.site',
                   'u1.u2.u3@domain.cloud']

invalid_email_lst = ['@domain.com',
                     'user@domain.c0m',
                     'user@domain.123',
                     'user@domain.companyyy',
                     'user@domain.c',
                     'user@domain-name.com',
                     'user@sub.domain.com',
                     'use@domain_.com',
                     'user-name@domain.com',
                     'user_name@domain.com',
                     'user+tag@domain.com',
                     'user!@domain.com',
                     'user.@domain.com',
                     '.user@domain.com']


@pytest.mark.parametrize('email', valid_email_lst)
def test_valid_email(email):
    assert is_email_valid(email) is True


@pytest.mark.parametrize('email', invalid_email_lst)
def test_invalid_email(email):
    assert is_email_valid(email) is False

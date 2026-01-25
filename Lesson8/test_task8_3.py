import pytest
from Lesson8.task8_3 import UserManager


@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_1_user_deleting(user_manager):
    manager = user_manager
    manager.remove_user("Alice")
    assert manager.get_all_users() == {"Bob": 25}


def test_user_already_exists(user_manager):
    manager = user_manager
    with pytest.raises(KeyError):
        manager.add_user("Alice", 45)


def test_get_all_users_not_empty(user_manager):
    manager = user_manager
    assert manager.get_all_users() == {"Alice": 30, "Bob": 25}


@pytest.mark.skipif(len(UserManager().get_all_users()) < 3,
                    reason="there is less than 3 users")
def test_there_is_no_user(user_manager):
    manager = user_manager
    assert len(manager.get_all_users()) == 2

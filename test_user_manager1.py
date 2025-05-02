import pytest
from user_manager import UserManager

@pytest.fixture()
def setup():
    user = UserManager()
    yield user
    user.users.clear()

def test_add_user(setup):
    setup.add_user(1, "Alice")
    assert setup.get_user(1) == "Alice"

def test_add_duplicate_user(setup):
    setup.add_user(1, "Alice")
    with pytest.raises(ValueError, "User exists"):
        setup.add_user(1, "Bob")

def test_delete_user(setup):
    setup.add_user(2, "hyce")
    setup.delete_user(2)
    assert setup.get_user(2) is None

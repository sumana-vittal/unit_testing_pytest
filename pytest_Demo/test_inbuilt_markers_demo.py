import sys

import pytest

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.parametrize("username,password",
                        [ ("selenium","webdriver"),
                         ("python","pytest"),
                         ("test123","testing")]
                         )
def test_valid_login(username,password):
    print(username, password)

@pytest.mark.skipif(sys.version_info<(3,13), reason="Not Supported")
def test_addproduct():
    print("add product")

@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver=None
@pytest.fixture()
def setup():
    print("start browser")
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test_1(setup):
    driver.get("https://www.google.com")
    print("test 1 executed")
    # print("close browser")

def test_2(setup):
    driver.get("https://www.facebook.com")
    print("test 2 executed")
    # print("close browser")

def test_3(setup):
    driver.get("https://www.github.com")
    print("test 3 executed")
    # print("close browser")
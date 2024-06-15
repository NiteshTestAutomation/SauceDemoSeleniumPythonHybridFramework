import pytest
from selenium import webdriver

from utilities import ReadConfiguration
@pytest.fixture()
def setup_and_teardown(request):
    browserName = ReadConfiguration.read_Configuaration("info", "browser")
    global driver
    driver = None
    if browserName.__eq__("chrome"):
     driver = webdriver.Chrome()
    elif browserName.__eq__("firefox"):
      driver = webdriver.Firefox()
    else:
      print("Browser driver not selected")
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.quit()
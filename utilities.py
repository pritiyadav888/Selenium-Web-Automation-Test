
from selenium import webdriver


def setup():
    driver = webdriver.Chrome(
        '/Users/ayadav/eclipse-workspace/fetchrewards-sdet/webdrivers/Darwin/chromedriver')


def teardown():
    driver.close()

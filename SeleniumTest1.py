# selenium.webdriver module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# the instance of WebDriver is created
driver = webdriver.Chrome(
    '/Users/ayadav/eclipse-workspace/fetchrewards-sdet/webdrivers/Darwin/chromedriver')


def teardown():
    driver.close()


def test_centennial_searchpage():
    # link of a website to explore the elements present in it
    driver.get("https://www.centennialcollege.ca/")

    driver.find_element_by_id('SearchTrigger').click()

    driver.find_element_by_id('txtSearch').send_keys("Artificial Intelligence")

    driver.find_element_by_id('btnSearch').click()

    urls = driver.find_elements_by_partial_link_text('Artificial Intelligence')

    for url in urls:
        assert "Artificial Intelligence" in url.text


def test_googlesearch():
    driver.get("https://www.google.com/")

    driver.find_element_by_name('q').send_keys("linkedin learning")
    driver.find_element_by_name('btnK').click()
    driver.find_elements_by_partial_link_text(
        'LinkedIn Learning with Lynda: Online Training Courses for ...').click()

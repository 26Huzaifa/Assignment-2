import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestWikipedia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.assertIn("Wikipedia, the free encyclopedia", driver.title)

        searchbar = driver.find_element(By.NAME, "search")
        searchbar.send_keys("Pakistan")
        searchbar.send_keys(Keys.RETURN)

        assert "There were no results matching the query." not in driver.page_source

    def test_create_account(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/w/index.php?title=Special:CreateAccount")
        self.assertIn("Wikipedia is made by people like you.", driver.page_source)

        name = driver.find_element(By.NAME, 'wpName')
        name.send_keys("Pakistani")

        password = driver.find_element(By.NAME, "wpPassword")
        password.send_keys("pakistanzindabad")

        retype_password = driver.find_element(By.NAME, "retype")
        retype_password.send_keys("pakistanzindabad")

        email = driver.find_element(By.NAME, "email")
        email.send_keys("pakistani@pakistan.com")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

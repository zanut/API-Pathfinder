import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(0.5)
    def test_index(self):
        self.driver.get("http://localhost:8000/html/")
        sleep(3)
        self.assertEqual("Traffic & Weather Data Visualization", self.driver.title)
        self.assertEqual(3, len(self.driver.find_elements(By.XPATH, "//a[@href]")))

    def test_navigation(self):
        self.driver.get("http://localhost:8000/html/")
        sleep(1)
        self.driver.find_element(By.ID, "link1").click()
        self.assertEqual("Average weather details by date", self.driver.title)
        self.driver.find_element(By.ID, "back").click()
        sleep(1)
        self.driver.find_element(By.ID, "link2").click()
        self.assertEqual("Average Weather Conditions (Past Week)", self.driver.title)
        self.driver.find_element(By.ID, "back").click()
        sleep(1)
        self.driver.find_element(By.ID, "link3").click()
        self.assertEqual("Traffic Condition", self.driver.title)
        self.driver.find_element(By.ID, "back").click()
        sleep(1)

    def test_daily_weather(self):
        self.driver.get("http://localhost:8000/html/")
        self.driver.find_element(By.ID, "link1").click()
        self.driver.implicitly_wait(1)
        self.choice = Select(self.driver.find_element(By.ID, "dataComboBox"))
        self.choice.select_by_index(2)
        self.driver.find_element(By.ID, "plotButton").click()
        self.driver.implicitly_wait(1)
        initial_div_count = len(self.driver.find_elements(By.XPATH, "//div[@class='plot']"))
        self.choice.select_by_index(3)
        self.driver.find_element(By.ID, "plotButton").click()
        self.driver.implicitly_wait(1)
        final_div_count = len(self.driver.find_elements(By.XPATH, "//div[@class='plot']"))
        self.assertEqual(initial_div_count, final_div_count)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()

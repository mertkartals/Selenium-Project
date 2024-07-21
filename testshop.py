import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.pazarium.com.tr/")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys("elbise")
        search_bar.send_keys(Keys.ENTER)

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/a/picture/img")))
        dress_image = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/a/picture/img")
        dress_image.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/a[1]/span")))
        size_selection = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/a[1]/span")
        size_selection.click()


        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID,"addToCartBtn")))
        dress_buy = driver.find_element(By.ID, "addToCartBtn")
        dress_buy.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div/div/div[1]/div/span")))
        confirmation_message = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div/div/div[1]/div/span")

        assert "Ürün Başarıyla Sepete Eklendi" in confirmation_message.text

        time.sleep(3)

    def tearDown(self):
        self.driver.close()




if __name__ == '__main__':
    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import math


n=int(input())
k=n/2
k=math.ceil(k)
print(k)

# link = "http://suninjuly.github.io/explicit_wait2.html"
# browser = webdriver.Chrome()
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     browser.get(link)
#
#     element = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'),"100"))
#     button = browser.find_element(By.XPATH, '//button[@id="book"]')
#     button.click()
#
#     x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
#     x = x_element.text
#     int(x)
#     y = calc(x)
#     input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
#     input1.send_keys(y)
#     button1 = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button1.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.XPATH, '//input[@id="country"]')
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button.click()
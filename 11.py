
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path=r'C:/Users/aitsanya/PLMX/Chromedriver/chromedriver.exe')
    browser.get(link)

    def func(x):
        return  str (math.log(abs(12 * math.sin(int(x)))))


    
    wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    buttonV = browser.find_element_by_id("book").click()

    x = int(browser.find_element_by_id("input_value").text)

    z=func(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(z)


    button = browser.find_element_by_id("solve")
    button.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()
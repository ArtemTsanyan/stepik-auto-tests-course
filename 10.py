
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path=r'C:/Users/aitsanya/PLMX/Chromedriver/chromedriver.exe')
    browser.get(link)

    def func(x):
        return  str (math.log(abs(12 * math.sin(int(x)))))

    button = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element_by_id("input_value").text)

    z=func(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(z)


    button = browser.find_element_by_tag_name("button")
    button.click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from time import *
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/explicit_wait2.html'
#select1 = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
#select1.select_by_value(str(sum))
# x = treasure_img.get_attribute('valuex')
# answer_input.send_keys(y)
# robot_checkbox.click()

#alert = browser.switch_to.alert
#alert.accept()
#confirm.dismiss()
#prompt.send_keys("My answer")
#prompt.accept()
#browser.switch_to.window(window_name)
#new_window = browser.window_handles[1]
#browser.execute_script("window.scrollBy(0, 100)")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), '100'))
    book_btn = browser.find_element(By.XPATH, "//*[@id='book']")
    book_btn.click()
    x = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    y = calc(x)
    browser.find_element(By.XPATH, "//*[@id='answer']").send_keys(y)
    browser.find_element(By.XPATH, "//*[@id='solve']").click()





finally:
    sleep(5)
    browser.quit()
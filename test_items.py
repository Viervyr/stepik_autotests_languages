from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(15)
    button = len(browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))
    time.sleep(10)
    assert button > 0, "There is no button!"

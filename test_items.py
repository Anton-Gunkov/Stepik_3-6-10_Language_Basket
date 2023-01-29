from selenium.common.exceptions import NoSuchElementException     
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "https://google.com"

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    btn_text = ""

    try:
        browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
        btn_text = browser.find_element(By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']").text
        print(f"\nButton 'Add to Basket' looks like (in current language): '{btn_text}'")
    except NoSuchElementException:
        print(f"\nButton 'Add to Basket' not found!")
    finally:
        assert btn_text != "", print("Button 'Add to Basket' have a problem")
    
    # better not to mix 'implicitly_wait' and 'time.sleep'
    time.sleep(15)
    

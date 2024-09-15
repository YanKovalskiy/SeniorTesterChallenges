# Написать тест, который заходит на страницу https://magento.softwaretestingboard.com/gear/bags.html и получает все цены товаров. Результат теста # должен быть таким: выводится на экран список (именно list в квадратных скобочках) всех цен со сраницы, причем цены должны быть без значка  #доллара (см. скрин).

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


def test_all_price(drv):
    locator = By.XPATH, "//*[@data-price-type='finalPrice']/span"

    prices = WDWait(drv, 10).until(ec.visibility_of_all_elements_located(locator))
    print([price.text[1:] for price in prices])
    # print([price.text.replace('$', '') for price in prices])

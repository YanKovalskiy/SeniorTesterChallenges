# 1. Зайти на сайт https://demoblaze.com/index.html
# 2. Кликнуть на товар Samsung galaxy s6
# 3. На странице товара нажать на кнопку Add to cart
# 4. Кликнуть Ок на всплывшем "Product added"
# 5. Еще раз нажать на кнопку Add to cart
# 6. Кликнуть Ок на всплывшем "Product added"
# 7. Кликнуть Cart в заголовке сайта
# 8. В корзине удалить один из добавленных товаров
# Ожидаемый результат:
# В корзине остался один товар.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

ITEM = 'Samsung galaxy s6'

LINK_SAMSUNG = By.XPATH, f"//a[text()='{ITEM}']"
LINK_CART = By.ID, "cartur"
LINKS_DELETE_FROM_CART = By.XPATH, "//a[text()='Delete']"
TITLE_ITEMS = By.XPATH, f"//td[text()='{ITEM}']"
BUTTON_ADD = By.XPATH, "//a[text()='Add to cart']"


def test_add_and_delete_from_cart(drv):
    wait = WebDriverWait(drv, 180)
    wait.until(es.element_to_be_clickable(LINK_SAMSUNG)).click()
    wait.until(es.element_to_be_clickable(BUTTON_ADD)).click()
    wait.until(es.alert_is_present()).accept()
    wait.until(es.element_to_be_clickable(BUTTON_ADD)).click()
    wait.until(es.alert_is_present()).accept()
    wait.until(es.element_to_be_clickable(LINK_CART)).click()
    link_delete_item = wait.until(es.element_to_be_clickable(LINKS_DELETE_FROM_CART))
    link_delete_item.click()
    wait.until(es.invisibility_of_element(link_delete_item))
    items = wait.until(es.visibility_of_all_elements_located(TITLE_ITEMS))
    assert len(items) == 1

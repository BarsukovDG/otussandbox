from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lessonSelenium.opencart.conftest import driver


def check_if_element_is_visible(driver, element, timeout=3):
    locator = (element['locator_type'], element['locator'])
    try:
        wait = WebDriverWait(driver, timeout=timeout)
        wait.until(EC.visibility_of_element_located(locator))
        return True
    except StaleElementReferenceException:
        return False


def wait_for_element_is_visible(driver, element, timeout=3):
    """
    Возвращает элемент, если он видим на странице

    Param element :: Указать переменную из модуля локаторов
    Param timeout :: Время ожидания локатора. Не рекомендуется ставить выше 5

    Прописать позже определение типа локатора в By.type
    """
    locator = (element['locator_type'], element['locator'])
    el = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located(locator),
                                                      message=f'Элемент {element} не появился на экране')
    return el


def wait_for_element_is_clickable(driver, element, timeout=3):
    """
        Возвращает элемент, если он кликабелен

        Param locator_type :: Указать тип локатора
        Param locator :: Указать локатор
        Param timeout :: Время ожидания локатора. Не рекомендуется ставить выше 5
        """
    locator = (element['locator_type'], element['locator'])
    el = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable(locator),
                                                      message=f'Не удалось кликнуть на элемент {element}')
    return el


def refresh_page(driver):
    driver.refresh()
    driver.implicitly_wait(1)


def wait_for_element_invisible(driver, element, timeout=3):
    locator = (element['locator_type'], element['locator'])
    el = WebDriverWait(driver, timeout=timeout).until(EC.invisibility_of_element(locator),
                                                      message=f'Элемент {element} не скрылся с экрана')


#todo заменить слип на другой тип ожидания после дебага
def wait(driver, timeout=1):
    # WebDriverWait(driver, timeout=timeout)
    sleep(timeout)

def get_elements(driver, element, timeout=3):
    locator = (element['locator_type'], element['locator'])
    WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
    el_list = driver.find_elements(*locator)
    return el_list


def scroll_to_element(driver, element):
    if wait_for_element_is_visible(driver, element, timeout=1):
        driver.execute_script("arguments[0].scrollIntoView();", element)
    else:
        pass


def scroll_to(driver, direction, step=1500):
    if direction == "down":
        driver.execute_script(f"window.scrollBy(0, {step});")
    elif direction == "up":
        driver.execute_script(f"window.scrollBy(0, -{step});")

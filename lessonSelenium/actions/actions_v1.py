from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lessonSelenium.opencart.conftest import driver


def wait_for_element_is_visible(element, timeout=3, driver=driver):
    """
    Возвращает элемент, если он видим на странице

    Param locator_type :: Указать тип локатора
    Param locator :: Указать локатор
    Param timeout :: Время ожидания локатора. Не рекомендуется ставить выше 5

    Прописать позже определение типа локатора в By.type
    """
    locator = (element['locator_type'], element['locator'])
    el = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located(locator),
        message=f'Элемент {element} не появился на экране')
    return el


def wait_for_element_is_clickable(locator, timeout=3, driver=driver):
    """
        Возвращает элемент, если он кликабелен

        Param locator_type :: Указать тип локатора
        Param locator :: Указать локатор
        Param timeout :: Время ожидания локатора. Не рекомендуется ставить выше 5
        """
    element = WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable(locator),
                                                           message=f'Не удалось кликнуть на элемент {locator}')
    return element


def refresh_page(driver=driver):
    driver.refresh()
    driver.implicitly_wait(1)

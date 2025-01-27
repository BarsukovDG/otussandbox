from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lessonSelenium.opencart.conftest import driver


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

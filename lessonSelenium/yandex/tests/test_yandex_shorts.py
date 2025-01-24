from lessonSelenium.yandex.pageObjects.locators import YandexZenLocators


def test_first(driver):
    shorts_btn = driver.find_element(*YandexZenLocators.shorts_locator)
    shorts_btn.click()
    assert 'Дзен' in driver.title

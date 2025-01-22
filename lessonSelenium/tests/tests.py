import time


def test_first(driver):
    base_page = driver.get('https://yandex.ru')
    shorts_locator = '/html/body/div[8]/div[2]/div[2]/div[1]/aside/ul/a[6]'
    shorts_btn = driver.find_element(by='xpath', value=shorts_locator)
    shorts_btn.click()
    assert 'Дзен' in driver.title
    time.sleep(5)

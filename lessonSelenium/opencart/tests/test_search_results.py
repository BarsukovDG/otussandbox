from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators as ocl
from lessonSelenium.actions import actions_v1


def test_login_opencart(driver):
    actions_v1.wait_for_element_is_visible(driver, element=ocl.search_bar)
    search_field = actions_v1.wait_for_element_is_visible(driver, element=ocl.search_field)
    search_field.clear()
    search_field.send_keys('Macbook')
    search_btn = actions_v1.wait_for_element_is_clickable(driver, element=ocl.search_btn)
    search_btn.click()
    actions_v1.wait_for_element_invisible(driver, element=ocl.load_ring, timeout=10)
    # проверка на бота проводится 1-2 раза, поэтому проверяю еще пару раз на исчезновение элемента
    actions_v1.wait_for_element_invisible(driver, element=ocl.load_ring, timeout=10)
    actions_v1.wait_for_element_invisible(driver, element=ocl.load_ring, timeout=10)
    result_card = actions_v1.wait_for_element_is_visible(driver, element=ocl.result_card)
    if not result_card:
        actions_v1.refresh_page(driver)
    result = driver.find_elements(by=ocl.card_name['locator_type'], value=ocl.card_name['locator'])
    result_text = []
    for _ in result:
        result_text.append(_.text().lower())
    for _ in result_text:
        assert 'macbook' in _

from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators as ocl
from lessonSelenium.actions import actions_v1


def test_login_opencart(driver):
    search_field = actions_v1.wait_for_element_is_visible(element=ocl.search_bar)
    search_field.clear()
    search_field.send_keys('Macbook')
    search_btn = actions_v1.wait_for_element_is_clickable(element=ocl.search_btn)
    search_btn.click()
    result_card = actions_v1.wait_for_element_is_visible(element=ocl.result_card)
    if not result_card:
        actions_v1.refresh_page()
    result_text = driver.find_elements(by=ocl.card_name['locator_type'], value=ocl.card_name['locator']).text()
    assert 'macboook' in result_text.lower()
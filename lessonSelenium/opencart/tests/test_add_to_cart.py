from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators as ocl
from lessonSelenium.actions import actions_v1


def test_add_to_cart(driver):
    actions_v1.wait_for_element_is_visible(driver, element=ocl.search_bar)
    actions_v1.scroll_to(driver, 'down', step=400)
    actions_v1.wait(driver, 3)
    a2c_btn = actions_v1.wait_for_element_is_clickable(driver, ocl.add_to_cart_btn)
    a2c_btn.click()
    actions_v1.wait(driver, 1)
    assert actions_v1.check_if_element_is_visible(driver, element=ocl.add_to_cart_alert)

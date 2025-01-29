from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators as ocl
from lessonSelenium.actions import actions_v1


def test_categories_bar(driver):
    height = driver.get_window_size().get('height')
    width = driver.get_window_size().get('width')
    driver.set_window_size(height=height, width=width/2)
    actions_v1.wait_for_element_is_visible(driver, ocl.menu_bar, timeout=3)
    header = actions_v1.wait_for_element_is_visible(driver, ocl.menu_header)
    header_text =header.text
    assert header_text == 'Categories'
    burger = actions_v1.wait_for_element_is_clickable(driver, ocl.menu_burger)
    actions_v1.wait(driver, timeout=1)
    burger.click()
    actions_v1.wait(driver, 1)
    categories = actions_v1.get_elements(driver, ocl.category_link, timeout=10)
    categories_name = []
    for c in categories:
        categories_name.append(c.text.lower())
    assert 'tablets' in categories_name

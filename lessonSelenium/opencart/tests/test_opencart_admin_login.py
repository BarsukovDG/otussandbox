from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators


def test_login_opencart(driver):
    driver.get('https://demo.opencart.com/admin/')
    username_input = driver.find_element(by=OpenCartLocators.username_input['locator_type'],
                                         value=OpenCartLocators.username_input['locator'])
    password_input = driver.find_element(by=OpenCartLocators.password_input['locator_type'],
                                         value=OpenCartLocators.password_input['locator'])
    login_btn = driver.find_element(by=OpenCartLocators.login_btn['locator_type'],
                                         value=OpenCartLocators.login_btn['locator'])
    username_input.clear()
    username_input.send_keys('demo')
    password_input.clear()
    password_input.send_keys('demo')
    login_btn.click()
    driver.implicitly_wait(2)
    assert driver.find_element(by=OpenCartLocators.profile_icon['locator_type'],
                                         value=OpenCartLocators.profile_icon['locator'])

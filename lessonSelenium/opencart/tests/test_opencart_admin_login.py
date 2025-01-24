from lessonSelenium.opencart.pageObjects.locators import OpenCartLocators


def test_login_opencart(driver):
    driver.get('https://demo.opencart.com/admin/')
    username_input = driver.find_element(*OpenCartLocators.username_input)
    password_input = driver.find_element(*OpenCartLocators.password_input)
    login_btn = driver.find_element(*OpenCartLocators.login_btn)
    username_input.clear()
    username_input.send_keys('demo')
    password_input.clear()
    password_input.send_keys('demo')
    login_btn.click()
    driver.implicitly_wait(2)
    assert driver.find_element(*OpenCartLocators.profile_icon)

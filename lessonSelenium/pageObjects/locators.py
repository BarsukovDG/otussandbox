from selenium.webdriver.common.by import By


class YandexZenLocators:
    shorts_locator = (By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[1]/aside/ul/a[6]')

class OpenCartLocators:
    username_input = (By.ID, 'input-username')
    password_input = (By.ID, 'input-password')
    login_btn = (By.XPATH, '/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button')
    profile_icon = (By.ID, 'nav-profile')
from selenium.webdriver.common.by import By


class OpenCartLocators:
    username_input = {'locator_type': By.ID,
                      'locator': 'input-username'}
    password_input = {'locator_type': By.ID,
                      'locator': 'input-password'}
    login_btn = {'locator_type': By.XPATH,
                 'locator': '/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button'}
    profile_icon = {'locator_type': By.ID,
                    'locator': 'nav-profile'}
    search_bar = {'locator_type': By.ID,
                  'locator': 'search'}
    search_field = {'locator_type': By.NAME,
                    'locator': 'search'}
    search_btn = {'locator_type': By.CSS_SELECTOR,
                  'locator': 'button.btn.btn-light.btn-lg'}
    result_card = {'locator_type': By.ID,
                   'locator': 'product-list'}
    card_name = {'locator_type': By.PARTIAL_LINK_TEXT,
                 'locator': 'search=macbook'}
    load_ring = {'locator_type': By.CSS_SELECTOR,
                 'locator': 'div.lds-ring'}
    menu_bar = {'locator_type': By.ID,
                 'locator': 'menu'}
    menu_header = {'locator_type': By.ID,
                 'locator': 'category'}
    menu_burger = {'locator_type': By.CSS_SELECTOR,
                 'locator': 'button.navbar-toggler'}
    category_link = {'locator_type': By.CSS_SELECTOR,
                 'locator': 'a.nav-link'} #a.nav-link.dropdown-toggle
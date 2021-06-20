from POM.Locators.locators import Locators as loc

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username = loc.username
        self.password = loc.password
        self.button = loc.button
        self.invalid_login = loc.invalid_login

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username).clear()
        self.driver.find_element_by_id(self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password).clear()
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.button).click()

    def check_invalid(self):
        msg = self.driver.find_element_by_xpath(loc.invalid_login).text
        return msg
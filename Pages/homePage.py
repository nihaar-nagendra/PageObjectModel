from POM.Locators.locators import Locators as loc

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome = loc.welcome
        self.logout = loc.logout

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome).click()

    def click_logout(self):
        self.driver.find_element_by_link_text("Logout").click()
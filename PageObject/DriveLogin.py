class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_xpath = "//input[@id='identifierId']"
        self.next_button_class_name = "VfPpkd-RLmnJb"
        self.password_textbox_xpath = "//input[@name='password']"
        self.pwd_next_button_xpath = "//div[@id='passwordNext']//div[2]"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_on_next_button(self):
        self.driver.find_element_by_class_name(self.next_button_class_name).click()

    def click_on_pwd_next_button(self):
        self.driver.find_element_by_xpath(self.pwd_next_button_xpath).click()
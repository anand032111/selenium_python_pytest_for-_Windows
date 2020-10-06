class GoogleDrivePage:

    def __init__(self, driver):
        self.driver = driver
        self.new_button_xpath = "//button[1]//div[2]"
        self.docs_link_xpath = "//html//body//div//div//div//div//span//span//div[contains(text(),'Google Docs')]"
        self.sheet_link_xpath = "//div[contains(text(),'Google Sheets')]"
        self.slide_link_xpath = "//div[contains(text(),'Google Slides')]"
        self.createFolder_link_xpath ="//body//div//div//div[1]//div[1]//span[2]//div[1]"
        self.enter_folder_title_xpath = "//body/div/div/div/input[1]"
        self.click_on_create_button_xpath = "//button[@name='ok']"
        self.file_upload_link_xpath = "//div[contains(text(),'File upload')]"

    def click_new_button(self):
        self.driver.find_element_by_xpath(self.new_button_xpath).click()

    def click_google_doc(self):
        self.driver.find_element_by_xpath(self.docs_link_xpath).click()

    def click_google_sheet(self):
        self.driver.find_element_by_xpath(self.sheet_link_xpath).click()

    def click_google_slide(self):
        self.driver.find_element_by_xpath(self.slide_link_xpath).click()

    def create_folder(self, title):
        self.driver.find_element_by_xpath(self.createFolder_link_xpath).click()
        self.driver.find_element_by_xpath(self.enter_folder_title_xpath).send_keys(title)
        self.driver.find_element_by_xpath(self.click_on_create_button_xpath).click()

    def file_upload(self):
        self.driver.find_element_by_xpath(self.file_upload_link_xpath).click()

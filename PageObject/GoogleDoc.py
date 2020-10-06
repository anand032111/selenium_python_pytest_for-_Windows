class DocHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.doc_title_css_selector = "input[class='docs-title-input']"
        self.document_title_xpath = "//*[@id='docs-title-widget']/input"
        self.click_on_insert_menu_xpath = "//div[@id='docs-insert-menu']"
        self.enter_text_xpath = "//body/div[@id='docs-editor-container']/div[@id='docs-editor']/div[" \
                                "@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[" \
                                "2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1] "
        self.click_on_chart = "//*[@id=':9z']/div/span[1]"
        # driver.find_element_by_css_selector("input[class='docs-title-input']").click()
        # driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Doc Experiment")
        self.click_on_sheet_insert_xpath="//div[@id='docs-insert-menu']"

    def click_on_title(self):
        self.driver.find_element_by_css_selector(self.doc_title_css_selector).click()

    def document_title(self, title):
        self.driver.find_element_by_xpath(self.document_title_xpath).send_keys(title)

    def enter_text(self, text):
        self.driver.find_element_by_xpath(self.enter_text_xpath).send_keys(text)

    def click_on_insert(self):
        self.driver.find_element_by_xpath(self.click_on_insert_menu_xpath).click()

    def click_on_chart(self):
        chart = self.driver.find_element_by_xpath(self.click_on_chart)

    def click_on_sheet_insert(self):
        self.driver.find_element_by_xpath(self.click_on_sheet_insert_xpath).click()

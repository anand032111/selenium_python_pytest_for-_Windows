import time
import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PageObject.DriveHomePage import GoogleDrivePage
from PageObject.GoogleDoc import DocHomePage
from utilities.BaseClass import BaseClass


class TestGoogleDrive(BaseClass):

    def test_Login_To_Google_Sheet(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        drive.click_google_sheet()
        print("Welcome to Google Sheet")
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.title)
        self.driver.find_element_by_css_selector("input[class='docs-title-input']").click()
        self.driver.implicitly_wait(3)
        act = ActionChains(self.driver)
        act.send_keys(Keys.BACKSPACE).perform()
        self.driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Sheet Experiment")
        act.send_keys(Keys.ENTER).perform()
        googledoc = DocHomePage(self.driver)
        googledoc.click_on_sheet_insert()
        time.sleep(3)
        act.send_keys((Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                       Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_RIGHT, Keys.ARROW_DOWN,
                       Keys.ENTER)).perform()
        time.sleep(5)
        sframe = self.driver.find_elements_by_tag_name("iframe")
        print("Number of frames availble ", len(sframe))
        self.driver.switch_to.frame(sframe[9])
        print("Frame switched")
        time.sleep(5)
        self.driver.find_element_by_xpath("//span[contains(text(),'browse')]").click()
        time.sleep(10)
        autoit.control_focus("Open", "")
        time.sleep(10)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\Dell\\Pictures\\google.jpg")
        time.sleep(10)
        autoit.control_click("Open", "Button1")
        time.sleep(15)
        print("A google Sheet is created in My drive with following content - 01 image")

    def test_Login_to_Google_Doc(self):
        drive = GoogleDrivePage(self.driver)
        time.sleep(2)
        drive.click_new_button()
        drive.click_google_doc()
        print("welcome to Google Doc")
        self.driver.switch_to.window(self.driver.window_handles[2])
        googledoc = DocHomePage(self.driver)
        googledoc.click_on_title()
        act = ActionChains(self.driver)
        act.send_keys(Keys.BACKSPACE).perform()
        googledoc.document_title("Automation Doc Experimet")
        act.send_keys(Keys.ENTER).perform()
        googledoc.click_on_insert()
        time.sleep(3)
        act.send_keys((Keys.ARROW_DOWN, Keys.ARROW_RIGHT, Keys.ENTER)).perform()
        time.sleep(5)
        autoit.control_focus("Open", "")
        time.sleep(10)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\Dell\\Pictures\\google.jpg")
        time.sleep(10)
        autoit.control_click("Open", "Button1")
        time.sleep(5)
        googledoc.click_on_insert()
        time.sleep(2)
        act1 = ActionChains(self.driver)
        act1.send_keys((Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_RIGHT, Keys.ARROW_RIGHT, Keys.ARROW_RIGHT,
                        Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)).perform()
        act1.send_keys(Keys.PAGE_DOWN, Keys.ENTER).perform()
        time.sleep(5)
        googledoc.click_on_insert()
        time.sleep(5)
        act2 = ActionChains(self.driver)
        act2.send_keys((Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_RIGHT,
                        Keys.ARROW_DOWN, Keys.ENTER)).perform()
        time.sleep(5)
        act2.send_keys(Keys.PAGE_DOWN, Keys.ENTER).perform()
        act2.send_keys("Google, LLC is an American multinational technology company that specializes in "
                       "Internet-related services and products, which include online advertising technologies, "
                       "a search engine, cloud computing, software, and hardware. ").perform()
        time.sleep(10)
        print("A google doc is created in your My drive with following content - 01 image, 01 table (3X3), 01 chart, "
              "01 drawing, 01 paragrah of 100-400 characters")

    def test_Login_to_Google_slides(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        drive.click_google_slide()
        print("welcome to Google Slide")
        self.driver.switch_to.window(self.driver.window_handles[2])
        print(self.driver.title)
        self.driver.find_element_by_css_selector("input[class='docs-title-input']").click()
        self.driver.implicitly_wait(3)
        act = ActionChains(self.driver)
        act.send_keys(Keys.BACKSPACE).perform()
        self.driver.find_element_by_xpath("//*[@id='docs-title-widget']/input").send_keys("Automation Slide Experiment")
        act.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        print("A google doc is created in your My drive")

    def test_Login_to_Google_createfolder(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        drive.create_folder("testcase6")
        drive.click_new_button()
        drive.create_folder("testcase7")
        time.sleep(5)
        print("Folder created and should be added to my drive.")

    def test_word_file_upload(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        time.sleep(5)
        drive.file_upload()
        time.sleep(5)
        autoit.control_focus("Open", "")
        time.sleep(15)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\Dell\\Desktop\\Gsuite.docx")
        time.sleep(10)
        autoit.control_click("Open", "Button1")
        time.sleep(3)
        print("A Non-google file is added to My drive")

    def test_image_file_upload(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        time.sleep(5)
        drive.file_upload()
        time.sleep(5)
        autoit.control_focus("Open", "")
        time.sleep(15)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\Dell\\Pictures\\google.jpg")
        time.sleep(10)
        autoit.control_click("Open", "Button1")
        time.sleep(3)
        print("Media file with extension .jpg should be added to  my drive.")

    def test_video_file_upload(self):
        drive = GoogleDrivePage(self.driver)
        drive.click_new_button()
        drive.file_upload()
        time.sleep(5)
        autoit.control_focus("Open", "")
        time.sleep(20)
        autoit.control_set_text("Open", "Edit1", "C:\\Users\\Dell\\Videos\\video1.mp4")
        time.sleep(10)
        autoit.control_click("Open", "Button1")
        time.sleep(5)
        print("Media file with extension .mp4 should be added to  my drive.")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BrowserOpener:

    def __init__ (self, executable_path, url):
        self.executable_path = executable_path
        self.url = url

    def get_driver(self):
        print("Starting browser")
        self.driver = webdriver.Firefox(executable_path = self.executable_path)

    def open_url(self, agree_button):
        self.driver.get(self.url)

        #  Click on 'I agree' button
        search = self.driver.find_elements_by_class_name(agree_button)
        search[1].click()

    def play_video(self, video_button):
        # Click on a random video
        video = self.driver.find_elements_by_class_name(video_button)
        sleep(7)
        video[0].click()

    def skip_ads(self, skip_button):
        while True:
            sleep(7)

            # Click on skip button
            try:
                ads = self.driver.find_element_by_class_name(skip_button)
                ads.click()
            except:
                break

    def close(self):
        self.driver.quit()
        print("Out of browser")
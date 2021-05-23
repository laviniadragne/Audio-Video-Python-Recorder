from selenium import webdriver
import threading
driver = webdriver.Firefox(executable_path='/home/lavinia/geckodriver')
url="https://www.youtube.com"
driver.get(url)


youtube_search = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/form/div/input")
youtube_search.send_keys("Latest Videos") #Searches for
#Click Search
clickButton = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/form/button")
clickButton.click()

assert "No results found." not in driver.page_source

skipAd = driver.find_element_by_xpath("xpath for next /html/body/div[2]/div[4]/div/div[4]/div[2]/div[2]/div/div[4]/div/div/div[5]/button")

def skipAdFunction():
    threading.Timer(3,skipAdFunction).start()
    if(skipAd.is_enabled() or skipAd.is_displayed()):
        skipAd.click()

skipAdFunction()

driver.close()
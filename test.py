from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import cv2
import numpy as np
import pyautogui

driver = webdriver.Firefox(executable_path='/home/lavinia/geckodriver')

driver.get('https://www.youtube.com')

search = driver.find_elements_by_class_name("lssxud")
search[1].click()


video = driver.find_elements_by_class_name("ytd-rich-item-renderer")
sleep(7)
video[0].click()


while True:
    sleep(7)
    try:
        ads = driver.find_element_by_class_name("ytp-ad-skip-button")
        ads.click()
    except:
        break


# display screen resolution, get it from your OS settings
# SCREEN_SIZE = pyautogui.size()
# # define the codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # create the video write object
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

# for i in range(200):
#     # make a screenshot
#     img = pyautogui.screenshot()
#     # convert these pixels to a proper numpy array to work with OpenCV
#     frame = np.array(img)
#     # convert colors from BGR to RGB
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     # write the frame
#     out.write(frame)
#     # show the frame
#     cv2.imshow("screenshot", frame)
#     # if the user clicks q, it exits
    
#     # if cv2.waitKey(1) == ord("q"):
#     #     break

# # make sure everything is closed when exited
# cv2.destroyAllWindows()
# out.release()


# sleep(10)
# driver.quit()

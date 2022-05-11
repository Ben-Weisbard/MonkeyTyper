from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://monkeytype.com/")

driver.find_element_by_class_name("buttons").click()

time.sleep(2)


def array(start):
    arr = []
    for x in range(start, 101):
        arr.append(driver.find_element_by_xpath("//div[@id='words']/div[" + str(x) + "]"))
    return arr


def itter(arr):
    for x in arr:
        pyautogui.write(x.text + " ")


def index(arr, counter, lastWord):
    for x in arr:
        counter = counter + 1
        print(counter)
        if driver.find_element_by_xpath("//div[@id='words']/div[" + str(counter) + "]").text == lastWord.text:
            return counter


found = False

arr = array(1)
itter(arr)
for x in range(0, 3):
    lastWord = arr[-1]
    counter = index(arr, 0, lastWord)
    arr = array(counter + 1)
    itter(arr)

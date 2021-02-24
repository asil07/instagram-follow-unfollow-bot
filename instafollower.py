from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "your driver path"
SIMILAR_ACCOUNT = "similar account username"
USERNAME = "your username"
PASSWORD = "your password"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        self.base_window = self.driver.window_handles[0]
        time.sleep(2)

    def login(self):
        insta_username = self.driver.find_element_by_name("username")
        insta_username.send_keys(USERNAME)
        insta_password = self.driver.find_element_by_name("password")
        insta_password.send_keys(PASSWORD)
        insta_password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_follower(self):
        search_profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]')
        search_profile.click()
        type_name = self.driver.find_element_by_css_selector(".LWmhU input")
        type_name.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        profile.click()
        time.sleep(5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        scr1 = self.driver.find_element_by_xpath('html/body/div[5]/div/div/div[2]')
        for n in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(1)
        pass

    def follow(self):

        follow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
        for fbutton in follow_buttons:
            try:
                fbutton.click()
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                continue
            else:
                time.sleep(1)

    def find_unfollow_page(self):
        profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
        profile.click()
        time.sleep(2)
        prof = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]')
        prof.click()
        time.sleep(2)
        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        time.sleep(2)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for n in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(1)
        pass

    def unfollow(self):
        unfollow_buttons = self.driver.find_elements_by_css_selector(".PZuss button")
        for item in unfollow_buttons:
            item.click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
            time.sleep(1)
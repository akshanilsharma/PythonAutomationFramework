from selenium import webdriver


class Login(object):

    def __init__(self,driver):
        self.driver = driver

    def username(self,username):
        self.driver.find_element_by_id("ap_email").clear()
        self.driver.find_element_by_id("ap_email").send_keys(username)

    def password(self,password):
        self.driver.find_element_by_id("ap_password").clear()
        self.driver.find_element_by_id("ap_password").send_keys(password)


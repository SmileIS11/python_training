# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class GroupCreationTest(unittest.TestCase):
    def setUp(self):
        s = Service('C:\\Users\\Igor\\PycharmProjects\\python_training\\drivers\\chromedriver.exe')
        self.wd = webdriver.Chrome(service=s)
        self.wd.implicitly_wait(60)

#"C:\\Users\\Igor\\PycharmProjects\\python_training\\drivers\\chromedriver.exe"
    def test_group_creation(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("admin")
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("secret")
        wd.find_element("id", "LoginForm").submit()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element("name", "new").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys("group")
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys("afafasf")
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys("aSFAF")
        wd.find_element("name", "submit").click()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
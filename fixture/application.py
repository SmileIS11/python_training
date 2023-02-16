from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        s = Service('/drivers/chromedriver.exe')
        self.wd = webdriver.Chrome(service=s)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")



    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element("name", "new").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contact_page()
        # init group creation
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.name)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(contact.address)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_home_page()


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()


    def destroy(self):
        self.wd.quit()
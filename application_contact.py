from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        s = Service('C:\\Users\\Igor\\PycharmProjects\\python_training\\drivers\\chromedriver.exe')
        self.wd = webdriver.Chrome(service=s)
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")


    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("id", "LoginForm").submit()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()


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


    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()
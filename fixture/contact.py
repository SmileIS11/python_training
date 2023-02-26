from selenium.webdriver.common.by import By
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_page()
        # init contact creation
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element("name", "submit").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        # init contact creation
        self.fill_contact_form(new_contact_data)
        # submit contact creation
        wd.find_element("name", "update").click()
        self.return_to_home_page()


    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # delete first contact
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        # select first checkbox
        wd.find_element("name", "selected[]").click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements("name", "selected[]"))

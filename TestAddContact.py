# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.wd
        self.open_home_page(driver)
        self.login(driver)
        self.add_new_contact(driver)
        self.logout(driver)

    def add_new_contact(self, wd):
        self.add_name_info(wd, Contact(firstname="Ivan", middlename="Alexey", lastname="Ivanov", nickname="IV"))
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Photograph")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("TAIS")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("ul. Lenina")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("28392")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("8944")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("98423")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("98428")
        self.add_email(wd)
        self.add_birthday(wd)
        self.add_anniversary(wd)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("ul. Mira")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("dont call")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("instagram:")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_email(self, wd):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("iv@mail.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("iv@gmail.ru")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("iv@yandex.ru")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("iv.ru")

    def add_anniversary(self, wd):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("17")
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("March")
        wd.find_element_by_xpath("(//option[@value='March'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2019")

    def add_birthday(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("14")
        wd.find_element_by_xpath("//option[@value='14']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")

    def add_name_info(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

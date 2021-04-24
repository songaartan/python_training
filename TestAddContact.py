# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Ivan")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Alexey")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Ivanov")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("Iv")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Photograph")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("TAIS")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("ul. Lenina")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("28392")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("8944")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("98423")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("98428")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("iv@mail.ru")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("iv@gmail.ru")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("iv@yandex.ru")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("iv.ru")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("14")
        driver.find_element_by_xpath("//option[@value='14']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.find_element_by_xpath("//option[@value='April']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("17")
        driver.find_element_by_xpath("(//option[@value='17'])[2]").click()
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("March")
        driver.find_element_by_xpath("(//option[@value='March'])[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2019")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("ul. Mira")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("dont call")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("instagram:")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, title, company, address):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address


        """
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

    def add_anniversary(self, driver):
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

    def add_birthday(self, driver):
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("14")
        driver.find_element_by_xpath("//option[@value='14']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.find_element_by_xpath("//option[@value='April']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
"""
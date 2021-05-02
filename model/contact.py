class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, title,
                 company, address, homephone, mobilephone, workphone, fax, address2,
                 phone2, notes, email, email2, email3, homepage,
                 bday, bmonth, byear, aday, amonth, ayear):
        # name
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        # company
        self.title = title
        self.company = company
        self.address = address
        # phones
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        # email
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        # birthday
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        # anniversary
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        # secondary info
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes



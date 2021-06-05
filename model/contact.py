from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None, fax=None, address2=None,
                 secondaryphone=None, notes=None, email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
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
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                                                 self.nickname, self.title, self.company,
                                                                 self.address, self.homephone, self.mobilephone,
                                                                 self.workphone, self.fax, self.email,
                                                                 self.email2, self.email3, self.homepage,
                                                                 self.bday, self.bmonth, self.byear,
                                                                 self.aday, self.amonth, self.ayear,
                                                                 self.address2, self.secondaryphone, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

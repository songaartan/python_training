# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_date(minday, maxday):
    return str(random.randrange(minday, maxday))

def random_month():
    monthes = ["January", "February", "March", "April", "May", "June", "Jule", "August", "September", "October", "November", "December"]
    return random.choice(monthes)

def random_year(minyear, maxyear):
    return random.randrange(minyear, maxyear)

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + \
           "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".ru"


testdata = [Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                                nickname=random_string("nickname", 10), title=random_string("title", 20),
                                company=random_string("company", 10), address=random_string("address", 10),
                                homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
                                workphone=random_string("workphone", 10), fax=random_string("fax", 10),
                                email=random_email("email", 10), email2=random_email("email2", 10),
                                email3=random_email("email3", 10), homepage=random_string("homepage", 10),
                                address2=random_string("address2", 10), secondaryphone=random_string("secondaryphone", 10), notes=random_string("notes", 40),
                                bday=random_date(1, 30), bmonth=random_month(), byear=random_year(1900, 2021),
                                aday=random_date(1, 30), amonth=random_month(), ayear=random_year(1900, 2021))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


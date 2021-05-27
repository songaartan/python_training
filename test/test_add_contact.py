# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Alexey", lastname="Ivanov",
                                nickname="IV", title="TITLE", company="TAIS", address="ul. Lenina",
                                homephone="28392", mobilephone="8944", workphone="98423", fax="98428",
                                email="iv@mail.ru", email2="iv@gmail.ru", email3="iv@yandex.ru", homepage="iv.ru",
                                address2="ul.mira", secondaryphone="3453443", notes="xxx",
                                bday="14", bmonth="April", byear="1990",
                                aday="22", amonth="March", ayear="2020")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


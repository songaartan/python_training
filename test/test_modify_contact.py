from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan", middlename="Alexey", lastname="Ivanov",
                                nickname="IV", title="", company="TAIS", address="",
                                homephone="28392", mobilephone="", workphone="98423", fax="",
                                email="iv@mail.ru", email2="", email3="", homepage="iv.ru",
                                address2="ul.mira", phone2="", notes="xxx", bday="10", bmonth="April", byear="1990",
                                aday="22", amonth="March", ayear="2020"))
    contact = Contact(firstname="Alexandr", middlename="Alexey", lastname="Sozinov",
                                nickname="Alex", title="NONAME", company="TAIS", address="ul. Lenina",
                                homephone="28392", mobilephone="8944", workphone="98423", fax="98428",
                                email="iv@mail.ru", email2="iv@gmail.ru", email3="iv@yandex.ru", homepage="iv.ru",
                                address2="ul.mira", phone2="1111111", notes="no notes",
                                bday="22", bmonth="April", byear="1998",
                                aday="22", amonth="May", ayear="2018")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


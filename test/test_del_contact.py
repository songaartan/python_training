from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Ivan", middlename="Alexey", lastname="Ivanov",
                                nickname="IV", title="", company="TAIS", address="",
                                homephone="28392", mobilephone="", workphone="98423", fax="",
                                email="iv@mail.ru", email2="", email3="", homepage="iv.ru",
                                address2="ul.mira", phone2="", notes="xxx", bday="10", bmonth="April", byear="1990",
                                aday="22", amonth="March", ayear="2020"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


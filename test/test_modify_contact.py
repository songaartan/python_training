from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Alexandr", middlename="Alexey", lastname="Sozinov",
                                nickname="Alex", title="NONAME", company="TAIS", address="ul. Lenina",
                                homephone="28392", mobilephone="8944", workphone="98423", fax="98428",
                                email="iv@mail.ru", email2="iv@gmail.ru", email3="iv@yandex.ru", homepage="iv.ru",
                                address2="ul.mira", phone2="1111111", notes="no notes",
                                bday="22", bmonth="April", byear="1998",
                                aday="22", amonth="May", ayear="2018"))
    app.session.logout()

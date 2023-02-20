from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name='Oleg'))
    app.session.logout()

def test_modify_contact_header(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company='New company'))
    app.session.logout()
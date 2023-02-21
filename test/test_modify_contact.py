from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="text"))
    app.contact.modify_first_contact(Contact(name='Oleg'))


def test_modify_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="text"))
    app.contact.modify_first_contact(Contact(company='New company'))

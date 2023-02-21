from model.contact import Contact

def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(name='Oleg'))


def test_modify_contact_header(app):
    app.contact.modify_first_contact(Contact(company='New company'))

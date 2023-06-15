import uuid


class Company:
    address = ''

    # is_private = False
    def __init__(self, id, title, email, website, phone):
        self.id = id
        self.title = title
        self.email = email
        self.website = website
        self.phone = phone


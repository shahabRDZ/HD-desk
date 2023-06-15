from .person import Person
import uuid


class Customer(Person):
    def __init__(self, id: int or None, fname: str, lname: str, email: str, phone: str, address: str, website: str,
                 job_title: str, user_id: int):
        super().__init__(fname, lname, email, phone)
        self.id = id
        self.address = address
        self.website = website
        self.job_title = job_title
        self.user_id = user_id

import uuid

from .person import Person


class Agent(Person):
    def __init__(self, id: int or None, company_id: uuid, fname: str, lname: str,
                 email: str, phone: str, division: str, emp_id: str, user_id: int) -> object:
        super().__init__(fname, lname, email, phone)
        self.id = id
        self.company_id = company_id
        self.division = division
        self.emp_id = emp_id
        self.user_id = user_id

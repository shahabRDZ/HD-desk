class Ticket:
    def __init__(self, id, title, desc, product, customer):
        self.title = title
        self.desc = desc
        self.product = product
        self.customer = customer

    def get_create_sql(self):
        sql_insert = f"""
            INSERT INTO [Ticket] 
                (title, desc, product, customer)
            VALUES
                ('{str(self.title)}', '{self.desc}', '{self.product}', '{self.customer}')
        """
        return sql_insert

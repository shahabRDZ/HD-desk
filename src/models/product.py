import json

class Product:
    def __init__(self, id, title, category, company_id, desc):
        self.id = id
        self.title = title
        self.category = category
        self.company_id = company_id
        self.desc = desc

    def get_create_sql(self):
        sql_insert = f"""
            INSERT INTO [Product]
                (title, category, company_id, desc)
            VALUES
                ('{self.title}', '{self.category}', '{self.company_id}', '{self.desc}')
        """
        return sql_insert

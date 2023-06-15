import sqlite3
from models.company import Company

class CompanyService:
    def __init__(self):
        self._db_name = 'hdesk.db'
        self._connection = sqlite3.connect(self._db_name)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def insert(self, company: Company):
        sql_insert = f"""
                    INSERT INTO [Company] 
                        (id, title, email, website, phone)
                    VALUES
                        ('{str(company.id)}', '{company.title}', '{company.email}', '{company.website}', '{company.phone}')
                """
        print(sql_insert)
        self._connection.execute(sql_insert)
        self._connection.commit()

    def update(self, company: Company):
        sql_update = f'''
                UPDATE [Company] SET 
                    [title] = '{company.title}',
                    [email] = '{company.email}',
                    [website] = '{company.website}',
                    [phone] = '{company.phone}'
                WHERE [id] = '{str(company.id)}'
        '''
        print(sql_update)
        self._connection.execute(sql_update)
        self._connection.commit()

    def delete(self, id):
        sql_delete = f'''
                DELETE FROM [Company] WHERE [id] = '{str(id)}'
        '''
        print(sql_delete)
        self._connection.execute(sql_delete)
        self._connection.commit()

    def get(self, id):
        sql = f"SELECT * FROM [Company] WHERE id = '{id}'"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        return Company(*data[0])

    def get_all(self):
        sql = 'SELECT * FROM [Company]'
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        print(data)
        return [Company(*item) for item in  data]

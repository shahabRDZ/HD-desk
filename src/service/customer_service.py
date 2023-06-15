import sqlite3
import uuid
from models.customer import Customer

class CustomerService:
    def __init__(self):
        self._db_name = 'hdesk.db'
        self._connection = sqlite3.connect(self._db_name)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def insert(self, customer: Customer):
        sql_insert = """
              INSERT INTO [Customer]
              ([fname], [lname], [email], [phone], [address], [website], [job_title],[user_id])
              VALUES
              (?, ?, ?, ?, ?, ?, ?, ?)
          """
        self._connection.execute(sql_insert, (
            customer.fname,
            customer.lname,
            customer.email,
            customer.phone,
            customer.address,
            customer.website,
            customer.job_title,
            customer.user_id
        ))
        self._connection.commit()

    def update(self, customer: Customer):
        sql_update = f'''
                UPDATE [customer] SET 
                    [fname] = '{customer.fname}',
                    [lname] = '{customer.lname}',
                    [email] = '{customer.email}',
                    [phone] = '{customer.phone}',
                    
                    [website] = '{customer.website}',
                    [job_title] = '{customer.job_title}'
                WHERE [user_id] = '{str(customer.user_id)}'
        '''
        print(sql_update)
        self._connection.execute(sql_update)
        self._connection.commit()

    def delete(self, id):
        sql_delete = f'''
                DELETE FROM [Customer] WHERE [id] = '{str(id)}'
        '''
        print(sql_delete)
        self._connection.execute(sql_delete)
        self._connection.commit()

    def get(self, id):
        sql = f"SELECT * FROM [Customer] WHERE id = '{id}'"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        return Customer(*data[0])

    def get_all(self):
        sql = 'SELECT * FROM [Customer]'
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        print(data)
        return [Customer(*item) for item in data]

import sqlite3


# Domain Models
# Encapsapluation

class Database:
    def __init__(self):
        self._db_name = 'hdesk.db'
        self._connection = sqlite3.connect(self._db_name)
        self._cursor = self._connection.cursor()

    def migrate(self):
        sql_company = """
            CREATE TABLE IF NOT EXISTS [Company]
            (
                [id] VARCHAR PRIMARY KEY,
                [title] VARCHAR(255) NOT NULL, 
                [email] VARCHAR(500),
                [website] VARCHAR(500),
                [phone] VARCHAR(12)
            )
        """
        self._connection.execute(sql_company)

        sql_user = """
                    CREATE TABLE IF NOT EXISTS [User]
                    (
                        [Id] INTEGER PRIMARY KEY AUTOINCREMENT,
                        [UserName] TEXT NOT NULL,
                        [Password] TEXT NOT NULL
                    )
                """
        self._connection.execute(sql_user)

        sql_product = """
            CREATE TABLE IF NOT EXISTS [Product]
            (
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [title] VARCHAR(255) NOT NULL,
                [category] VARCHAR(255),
                [desc] VARCHAR(1000),
                [company_id] VARCHAR NOT NULL,
                FOREIGN KEY (company_id) REFERENCES Company(id)
            )
        """
        self._connection.execute(sql_product)

        sql_agent = """
              CREATE TABLE IF NOT EXISTS [Agent]
               (
                    [Id] INTEGER PRIMARY KEY AUTOINCREMENT,
                    [fname] VARCHAR(255) NOT NULL,
                    [lname] VARCHAR(255),
                    [email] VARCHAR(500),
                    [phone] VARCHAR(12),
                    [division] TEXT,
                    [emp_id] TEXT,
                    [user_id] INTEGER NOT NULL,
                    [company_id] TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES User(id),
                    FOREIGN KEY (company_id) REFERENCES Company(id)
                )
        """
        self._connection.execute(sql_agent)

        sql_customer = """
                      CREATE TABLE IF NOT EXISTS [Customer]
                       (
                           [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                           [fname] VARCHAR(255) NOT NULL,
                           [lname] VARCHAR(255),
                           [email] VARCHAR(500),
                           [phone] VARCHAR(12),
                           [address] VARCHAR(500),
                           [website] VARCHAR,
                           [job_title] VARCHAR,
                           [user_id] INTEGER NOT NULL,
                           FOREIGN KEY (user_id) REFERENCES User(id)
                       )
         """
        self._connection.execute(sql_customer)

        sql_ticket = """
                 CREATE TABLE IF NOT EXISTS [Ticket]
                  (
                       [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                       [company_id] TEXT NOT NULL, 
                       [title] TEXT NOT NULL,
                       [desc] TEXT NOT NULL,
                       [product_id] INTEGER NULL,
                       [customer_id] INTEGER NOT NULL,
                       FOREIGN KEY (company_id) REFERENCES Company(id),
                       FOREIGN KEY (product_id) REFERENCES Product(id),
                       FOREIGN KEY (customer_id) REFERENCES Customer(id)
                  )
        """
        self._connection.execute(sql_ticket)

        sql_ticket_reply = """
                CREATE TABLE IF NOT EXISTS [Ticket_Reply]
                (
                    [Id] INTEGER PRIMARY KEY AUTOINCREMENT,
                    [ticket_id] INTEGER NOT NULL,
                    [user_id] INTEGER NOT NULL,
                    [desc] TEXT NOT NULL,
                    FOREIGN KEY (ticket_id) REFERENCES Ticket(id),
                    FOREIGN KEY (user_id) REFERENCES User(id)
                )
        """
        self._connection.execute(sql_ticket_reply)

    def exec(self, sql):
        self._connection.execute(sql)
        self._connection.commit()

    def get_company_by_id(self, id):
        sql = f"SELECT * FROM [Company] WHERE id = '{id}'"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        return data[0]

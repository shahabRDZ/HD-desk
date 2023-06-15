import sqlite3
import uuid
from models.agent import Agent
from models.company import Company

class AgentService:
    def __init__(self):
        self._db_name = 'hdesk.db'
        self._connection = sqlite3.connect(self._db_name)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def get_by_company(self, company_id: uuid.uuid4()):
        sql = f"SELECT * FROM [Agent] WHERE [company_id] = '{str(company_id)}'"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        print(data)
        return [Agent(*item) for item in data]

    def insert(self, agent: Agent):
        sql_insert = """
            INSERT INTO [Agent]
            ([company_id], [fname], [lname], [email], [phone], [division], [emp_id], [user_id])
            VALUES
            ( ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self._connection.execute(sql_insert, [
            agent.company_id,
            agent.fname,
            agent.lname,
            agent.email,
            agent.phone,
            agent.division,
            agent.emp_id,
            agent.user_id
        ])
        self._connection.commit()



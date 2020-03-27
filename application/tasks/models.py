from application import db
from application.models import Base
from sqlalchemy.sql import text 
from datetime import datetime


class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(350), nullable=False)
    estimatedTime = db.Column(db.Numeric(10, 1), nullable=False)
    actualTime = db.Column(db.Numeric(10, 1), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __init__(self, name, content, estimatedTime, actualTime, date, status):
        self.name = name
        self.content = content
        self.estimatedTime = estimatedTime
        self.date = date
        self.status = status
        self.actualTime = actualTime


    @staticmethod
    def find_my_tasks(current_id, project_id):

        stmt = text("SELECT Task.name, Task.status, Task.date_created, Task.date, Task.id FROM Task"
                    " LEFT JOIN Project ON Project.id = Task.project_id"
                    " WHERE Task.account_id = :current_id"
                    " AND Task.project_id = :project_id"
                    " GROUP BY Task.id"
                    ).params(current_id=current_id, project_id=project_id)

        res = db.engine.execute(stmt)
        tasks = []

        for row in res:
            tasks.append({ 'name': row[0], 'status': row[1], 'createDate': row[2], 'comDate': row[3], 'id': row[4] })

        return tasks

    @staticmethod
    def find_project_participants(project_id):

        stmt = text("SELECT Account.id, Account.name, COUNT(Account.id) FROM Registration"
                    " LEFT JOIN Account ON Registration.account_id = Account.id"
                    " WHERE Registration.project_id = :project_id"
                    " GROUP BY Account.name"
                    ).params(project_id=project_id)

        res = db.engine.execute(stmt)
        data = []

        for row in res:
            data.append({ 'accountId': row[0], 'name': row[1] })

        return data


    @staticmethod
    def find_tasks_of_participant(project_id, account_id):

        stmt1 = text("SELECT COUNT(Task.id) from Task"
                    " LEFT JOIN Project ON Project.id = Task.project_id"
                    " LEFT JOIN Account ON Account.id = Task.account_id"
                    " WHERE Project.id = :project_id"
                    " AND Account.id = :account_id"
                    " AND Task.status = 0"
                    ).params(project_id=project_id, account_id=account_id)

        stmt2 = text("SELECT COUNT(Task.id) from Task"
                    " LEFT JOIN Project ON Project.id = Task.project_id"
                    " LEFT JOIN Account ON Account.id = Task.account_id"
                    " WHERE Project.id = :project_id"
                    " AND Account.id = :account_id"
                    " AND Task.status = 1"
                    ).params(project_id=project_id, account_id=account_id)

        res1 = db.engine.execute(stmt1)
        res2 = db.engine.execute(stmt2)

        taskData = []

        for row in res1:
            taskData.append({ 'uncom': row[0] })

        for row in res2:
            taskData.append({ 'com': row[0] })

        return taskData

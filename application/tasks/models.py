from application import db
from application.models import Base
from sqlalchemy.sql import text
from datetime import datetime
import os


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

        if os.environ.get('HEROKU'):
            for row in res:
                tasks.append({ 'name': row[0], 'status': row[1], 'createDate': row[2].date(), 'comDate': row[3], 'id': row[4] })
        else:
            for row in res:
                tasks.append({ 'name': row[0], 'status': row[1], 'createDate': row[2][:10], 'comDate': row[3], 'id': row[4] })

        return tasks

    @staticmethod
    def find_project_participants(project_id):

        stmt = text("SELECT Account.id, Account.name FROM Registration"
                    " LEFT JOIN Account ON Registration.account_id = Account.id"
                    " WHERE Registration.project_id = :project_id"
                    " GROUP BY Account.id"
                    ).params(project_id=project_id)

        res = db.engine.execute(stmt)
        data = []

        for row in res:
            data.append({'accountId': row[0], 'name': row[1]})

        return data

    @staticmethod
    def find_tasks_of_participant(project_id, account_id):

        stmt1 = text("SELECT COUNT(Task.id) from Task"
                     " LEFT JOIN Project ON Project.id = Task.project_id"
                     " LEFT JOIN Account ON Account.id = Task.account_id"
                     " WHERE Project.id = :project_id"
                     " AND Account.id = :account_id"
                     " AND Task.status = False"
                     ).params(project_id=project_id, account_id=account_id)

        stmt2 = text("SELECT COUNT(Task.id) from Task"
                     " LEFT JOIN Project ON Project.id = Task.project_id"
                     " LEFT JOIN Account ON Account.id = Task.account_id"
                     " WHERE Project.id = :project_id"
                     " AND Account.id = :account_id"
                     " AND Task.status = True"
                     ).params(project_id=project_id, account_id=account_id)

        stmt3 = text("SELECT COUNT(Task.id) from Task"
                     " LEFT JOIN Project ON Project.id = Task.project_id"
                     " LEFT JOIN Account ON Account.id = Task.account_id"
                     " WHERE Project.id = :project_id"
                     " AND Account.id = :account_id"
                     ).params(project_id=project_id, account_id=account_id)


        res1 = db.engine.execute(stmt1)
        res2 = db.engine.execute(stmt2)
        res3 = db.engine.execute(stmt3)


        taskData = []

        for row in res1:
            taskData.append({'uncom': row[0]})

        for row in res2:
            taskData.append({'com': row[0]})

        for row in res3:
            taskData.append({'total': row[0]})

        return taskData

    @staticmethod
    def time_of_project(project_id):
        stmt = text("SELECT SUM(Task.'estimatedTime'), SUM(Task.'actualTime') FROM Task"
                    " LEFT JOIN Project ON Project.id = Task.project_id"
                    " WHERE Project.id = :project_id"
                    ).params(project_id=project_id)

        res = db.engine.execute(stmt)

        timeProject = []

        for row in res:
            timeProject.append({ 'estimated': row[0], 'actual': row[1] })

        return timeProject

    @staticmethod
    def time_of_person(project_id, account_id):
        stmt = text("SELECT SUM(Task.'estimatedTime'), SUM(Task.'actualTime') FROM Task"
                    " LEFT JOIN Account ON Account.id = Task.account_id"
                    " LEFT JOIN Project ON Project.id = Task.project_id"
                    " WHERE Account.id = :account_id"
                    " AND Project.id = :project_id"
                    ).params(project_id=project_id, account_id=account_id)

        res = db.engine.execute(stmt)
        
        timePerson = []

        for row in res:
            timePerson.append({ 'estimated': row[0], 'actual': row[1] })

        return timePerson

    @staticmethod
    def time_of_one_week(project_id, fromDate, toDate, account_id):

        if account_id is not None:
            stmt = text("SELECT SUM(Task.'estimatedTime'), SUM(Task.'actualTime') FROM Task"
                        " LEFT JOIN Project ON project.id = Task.project_id"
                        " WHERE project.id = :project_id"
                        " AND Task.date_modified >= :fromDate::date"
                        " AND Task.date_modified <= :toDate::date"
                        " AND Task.account_id = :account_id"
                        ).params(project_id=project_id, 
                                fromDate=fromDate, 
                                toDate=toDate,
                                account_id=account_id)
        else:
            stmt = text("SELECT SUM(Task.'estimatedTime'), SUM(Task.'actualTime') FROM Task"
                        " LEFT JOIN Project ON project.id = Task.project_id"
                        " WHERE project.id = :project_id"
                        " AND Task.date_modified >= :fromDate::date"
                        " AND Task.date_modified <= :toDate::date"
                        ).params(project_id=project_id, 
                                fromDate=fromDate, 
                                toDate=toDate)

        res = db.engine.execute(stmt)
        timeWeek = []

        for row in res:
            timeWeek.append({ 'estimated': row[0], 'actual': row[1] })

        return timeWeek
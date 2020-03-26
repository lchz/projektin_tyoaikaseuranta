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

        stmt = text("SELECT Task.name, Task.status FROM Task"
                    " LEFT JOIN Project ON Project.id = :project_id"
                    " WHERE Task.account_id = :current_id"
                    " GROUP BY Task.id"
                    ).params(current_id=current_id, project_id=project_id)

        res = db.engine.execute(stmt)
        tasks = []

        for row in res:
            tasks.append({ 'name': row[0], 'status': row[1] })

        return tasks

    @staticmethod
    def find_project_participants(project_id):
        stmt = text("SELECT Account.name FROM Account"
                    " LEFT JOIN registration ON project_id = :project_id"
                    " WHERE Account.id = registration.account_id"
                    " GROUP BY Account.name"
                   ).params(project_id=project_id)

        res = db.engine.execute(stmt)

        names = []

        for row in res:
            names.append({ 'name': row[0] })

        return names

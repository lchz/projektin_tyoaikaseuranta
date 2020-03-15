from application import db
from application.models import Base


class Task(Base):
   
    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(350), nullable=False)
    estimatedTime = db.Column(db.Numeric(10, 1), nullable=False)
    actualTime = db.Column(db.Numeric(10, 1), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)


    def __init__(self, name, content, estimatedTime, date, status):
        self.name = name
        self.content = content
        self.estimatedTime = estimatedTime
        self.date = date
        self.status = status

        self.actualTime = 0

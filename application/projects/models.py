from application import db
from application.models import Base
from sqlalchemy.sql import text


class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    # project master
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    tasks = db.relationship('Task', backref='project', lazy=True)

    # participants

    def __init__(self, name, description):
        self.name = name
        self.description = description


    @staticmethod
    def remove_project(project_id):
        stmtDeleteTasks = text("DELETE FROM Task"
                                " WHERE Task.project_id = :project_id"
                              ).params(project_id=project_id)

        stmtRemoveParticipants = text("DELETE FROM registration"
                                    " WHERE project_id = :project_id"
                                    ).params(project_id=project_id)

        stmtDeleteProject = text("DELETE FROM Project"
                                " WHERE Project.id = :project_id"
                                ).params(project_id=project_id)

        db.engine.execute(stmtDeleteTasks)
        db.engine.execute(stmtRemoveParticipants)
        db.engine.execute(stmtDeleteProject)

        
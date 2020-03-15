from application import db
from application.models import Base


class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    # creator / project master
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    tasks = db.relationship('Task', backref='project', lazy=True)
    
    # participants

    def __init__(self, name, description):
        self.name = name
        self.description = description

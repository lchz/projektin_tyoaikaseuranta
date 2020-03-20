from application import db
from application.models import Base

registration_table = db.Table('registration',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'account'

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    roles = db.Column(db.String(144), nullable=False)

    tasks = db.relationship('Task', backref='account', lazy=True)
    
    registrations = db.relationship('Project', 
                                    secondary=registration_table, 
                                    backref=db.backref('participants', lazy=True), 
                                    lazy=True )

    # Only MASTER can create projects
    created_projects = db.relationship('Project', backref='account', lazy=True)


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_roles(self):
        return self.roles

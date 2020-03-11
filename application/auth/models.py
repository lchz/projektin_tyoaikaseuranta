from application import db

registration_table = db.Table('registration',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship('Task', backref='account', lazy=True)
    
    registrations = db.relationship('Project', 
                                    secondary=registration_table, 
                                    backref=db.backref('participants', lazy=True), 
                                    lazy=True )


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

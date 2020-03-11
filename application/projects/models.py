from application import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    # creator / project master
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    tasks = db.relationship('Task', backref='project', lazy=True)
    
    # participants

    def __init__(self, name, description):
        self.name = name
        self.description = description

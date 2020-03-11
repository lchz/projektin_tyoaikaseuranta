from application import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), 
                                onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(350), nullable=False)
    estimatedTime = db.Column(db.Numeric(10, 1), nullable=False)
    actualTime = db.Column(db.Numeric(10, 1), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, content, estimatedTime, date, status):
        self.name = name
        self.content = content
        self.estimatedTime = estimatedTime
        self.date = date

        self.actualTime = 0
        self.status = False

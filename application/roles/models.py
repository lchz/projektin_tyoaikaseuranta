from application import db
from application.models import Base


class Role(Base):
    name = db.Column(db.String(50), unique=True)
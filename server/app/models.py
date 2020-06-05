from app import db


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_code = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Float, nullable=False)
    location = db.Column(db.Integer, nullable=False)

    def __init__(self, student_code, timestamp, location):
        self.student_code = student_code
        self.timestamp = timestamp
        self.location = location
        
    def __repr__(self):
        return f"<User('{self.student_code}', '{str(self.timestamp)}', '{str(self.location)}')>"

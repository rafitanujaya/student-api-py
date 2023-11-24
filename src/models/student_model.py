from config import db, ma

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    class_number = db.Column('class', db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())


class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        sqla_session = db.session

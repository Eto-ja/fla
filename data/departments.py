import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Departments(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    departments_id = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey("users.id"))
    department = orm.relationship('User')

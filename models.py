from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Table, Column, ForeignKey


class Model(DeclarativeBase):
    pass


class UserGood(Model):
    __tablename__ = "user_goods"
    user_id = Column(ForeignKey("users.id"), primary_key=True)
    good_id = Column(ForeignKey("goods.id"), primary_key=True)
    count: Mapped[int]


class User(Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Good(Model):
    __tablename__ = "goods"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

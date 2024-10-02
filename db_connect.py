from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Model, User, Good

engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/testdb", echo=True)


def create_tables():
    Model.metadata.create_all(engine)


def init_tables():
    with Session(bind=engine) as session:
        user1 = User(name="Terminator T-1000")
        user2 = User(name="David Bowie")
        user3 = User(name="Killmister")
        user4 = User(name="John Doe")

        good1 = Good(name="Мотоцикл")
        good2 = Good(name="Пулемёт Гатлинг")
        good3 = Good(name="Микрофон")
        good4 = Good(name="Виски")

        session.add_all([user1, user2, user3, user4, good1, good2, good3, good4])
        session.commit()

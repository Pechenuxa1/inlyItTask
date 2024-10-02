from sqlalchemy.orm import Session
from fastapi import HTTPException
from db_connect import engine
from models import UserGood, User, Good
from schemas import UserGoodDto
from sqlalchemy import select

class UserGoodRepository:

    @classmethod
    def add_good_to_user(cls, user_good_dto: UserGoodDto):
        with Session(engine) as session:
            if session.execute(select(User).where(User.id == user_good_dto.user_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.user_id} doesnt exist!")
            if session.execute(select(Good).where(Good.id == user_good_dto.good_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.good_id} doesnt exist!")

            db_user_good = session.execute(
                select(UserGood).where(
                    UserGood.user_id == user_good_dto.user_id
                ).where(
                    UserGood.good_id == user_good_dto.good_id
                )
            ).scalars().one_or_none()
            if db_user_good is None:
                session.add(UserGood(user_id=user_good_dto.user_id, good_id=user_good_dto.good_id, count=user_good_dto.count))
                session.commit()
                return user_good_dto
            else:
                db_user_good.count += user_good_dto.count
                session.commit()
                return UserGoodDto(user_id=db_user_good.user_id, good_id=db_user_good.good_id, count=db_user_good.count)

    @classmethod
    def del_good_from_user(cls, user_good_dto: UserGoodDto):
        with Session(engine) as session:
            if session.execute(select(User).where(User.id == user_good_dto.user_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.user_id} doesnt exist!")
            if session.execute(select(Good).where(Good.id == user_good_dto.good_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.good_id} doesnt exist!")

            db_user_good = session.execute(
                select(UserGood).where(
                    UserGood.user_id == user_good_dto.user_id
                ).where(
                    UserGood.good_id == user_good_dto.good_id
                )
            ).scalars().one_or_none()
            if db_user_good is None:
                session.add(UserGood(user_id=user_good_dto.user_id, good_id=user_good_dto.good_id, count=0))
                session.commit()
                return UserGoodDto(user_id=user_good_dto.user_id, good_id=user_good_dto.good_id, count=0)
            else:
                db_user_good.count -= user_good_dto.count
                if db_user_good.count < 0:
                    db_user_good.count = 0
                session.commit()
                return UserGoodDto(user_id=db_user_good.user_id, good_id=db_user_good.good_id, count=db_user_good.count)

    @classmethod
    def update_goods_user(cls, user_good_dto: UserGoodDto):
        with Session(engine) as session:
            if session.execute(select(User).where(User.id == user_good_dto.user_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.user_id} doesnt exist!")
            if session.execute(select(Good).where(Good.id == user_good_dto.good_id)).scalars().one_or_none() is None:
                raise HTTPException(400, f"User id {user_good_dto.good_id} doesnt exist!")

            db_user_good = session.execute(
                select(UserGood).where(
                    UserGood.user_id == user_good_dto.user_id
                ).where(
                    UserGood.good_id == user_good_dto.good_id)
            ).scalars().one_or_none()
            if db_user_good is None:
                session.add(UserGood(
                    user_id=user_good_dto.user_id,
                    good_id=user_good_dto.good_id,
                    count=user_good_dto.count)
                )
                session.commit()
                return user_good_dto
            else:
                db_user_good.count = user_good_dto.count
                session.commit()
                return UserGoodDto(user_id=db_user_good.user_id, good_id=db_user_good.good_id,
                                   count=db_user_good.count)
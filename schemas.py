from fastapi import HTTPException

from pydantic import BaseModel, field_validator


class UserGoodDto(BaseModel):
    user_id: int
    good_id: int
    count: int

    @field_validator("count")
    @classmethod
    def count_must_be_positive(cls, count):
        if count < 0:
            raise HTTPException(status_code=400, detail="Count must be positive!")
        else:
            return count

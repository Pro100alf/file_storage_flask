from typing import Generic, Optional, TypeVar

from app.models import db

ModelType = TypeVar("ModelType", bound=db.Model)


class Base(Generic[ModelType]):

    def __init__(self, model):
        self.__model = model

    def get_all(self) -> list[ModelType]:
        return self.__model.query.all()

    def _get_all_where(self, **filters) -> list[ModelType]:
        return self.__model.query.filter(
            *[getattr(self.__model, key) == value for key, value in filters.items()]
        ).all()

    def _get_where(self, **filters) -> Optional[ModelType]:
        return self.__model.query.filter(
            *[getattr(self.__model, key) == value for key, value in filters.items()]
        ).one_or_none()
import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Boolean


Base = declarative_base()


class IdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class NameMixin:
    name = Column(String, nullable=False)


class UrlMixin:
    url = Column(String, nullable=False, unique=True)

 tag_post = Table(
        "tag_post",
        Base.metadata,
        Column("post_id", Integer, ForeignKey("post.id")),
        Column("tag_id", Integer, ForeignKey("tag.id")),
    )

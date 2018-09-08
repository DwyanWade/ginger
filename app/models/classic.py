"""
Created on 2018/8/1 23:44

"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__Author__ = '阿强'


class Classic(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(50))
    fav_nums = Column(Integer, default=0)
    image = Column(String(100))
    index = Column(Integer, autoincrement=True)
    like_status = Column(Integer, default=0)
    pubdate = Column(String)
    title = Column(String(50), default="未名")
    type = Column(Integer)

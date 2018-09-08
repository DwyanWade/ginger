"""
Created on 2018/8/3 0:12

"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__Author__ = '阿强'


class Like(Base):
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
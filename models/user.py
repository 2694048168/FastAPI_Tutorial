#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: user.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:37
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from . import Base


# 创建 ORM 模型
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[String] = mapped_column(String(100), unique=True, index=True)
    username: Mapped[String] = mapped_column(String(100))
    password: Mapped[String] = mapped_column(String(200))
    mobile: Mapped[String] = mapped_column(String(100))

    # 一对一 uselist==false
    user_extension: Mapped["UserExtension"] = relationship(back_populates="user", uselist=False)
    # 一对多 关系
    articles: Mapped[List["Article"]] = relationship(back_populates="author")


# 和 user model 一对一关系
class UserExtension(Base):
    __tablename__ = "user_extension"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    university: Mapped[String] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="user_extension")

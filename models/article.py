#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: article.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:38
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from . import Base


# 和 user model 一对多关系
class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(100))
    content: Mapped[String] = mapped_column(Text)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), unique=True)
    author: Mapped["User"] = relationship(back_populates="articles")

    tags: Mapped[List["Tag"]] = relationship("Tag",
                                             back_populates="articles",
                                             secondary="article_tag")


# 多对多关系
class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))

    articles: Mapped[List["Article"]] = relationship("Article",
                                                     back_populates="tags",
                                                     secondary="article_tag")


class ArticleTag(Base):
    __tablename__ = "article_tag"

    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tag.id"), primary_key=True)

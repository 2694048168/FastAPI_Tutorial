#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: __init__.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:37
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

from settings import DB_URL

engine = create_engine(DB_URL,
                       echo=True,  # SQL 日志
                       pool_size=10,
                       max_overflow=20,
                       pool_recycle=3600,  # 默认 -1 表示永不回收
                       pool_timeout=10,  # unit 10s
                       pool_pre_ping=True)

AsyncFactory = sessionmaker(bind=engine,
                            class_=AsyncSession,
                            autoflush=True,
                            expire_on_commit=False)


# 定义命名约定的 Base 类
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })

# 导入信息
from . import user
from . import article

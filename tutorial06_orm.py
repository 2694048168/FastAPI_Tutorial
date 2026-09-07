#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial06_orm.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:17
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: ORM(Object Relational Mapper)
"""

"""
SQLAlchemy ORM: https://www.sqlalchemy.org/
ORM SQLModel: https://sqlmodel.tiangolo.com/

# 异步范式
pip install "sqlalchemy[asyncio]" # ORM 框架
pip install aiomysql # SQL 驱动支持
pip install cryptography # 连接 MySQL 加密处理

uv add "sqlalchemy[asyncio]"
uv add aiomysql
uv add cryptography

uv add "sqlalchemy[asyncio]" aiomysql cryptography

DB_URL = "mysql+aiomysql://user:password@host:port/db_name?charset=utf8mb4"
1. 配置连接 URL
2. 创建 engine
3. 创建会话 session
4. 创建 ORM model
5. 迁移模型到数据表 database via alembic Library
pip install alembic
uv add alembic

# 1. 创建迁移仓库
$ alembic init alembic --template async
# 2. 修改 alembic.ini 配置文件
# - 注释 其中的 sqlalchemy.url
# - 修改 env.py 添加连接数据库的配置 & target_metadata = Base.metadata
# 3. 生成迁移脚本(修改model后重新执行即可)
$ alembic revision --autogenerate -m "init"
# 4. 执行迁移脚本(修改model后重新执行即可)
$ alembic upgrade head

# script command: uvicorn tutorial06_orm:app --reload
"""

from fastapi import FastAPI
import models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

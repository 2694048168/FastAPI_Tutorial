#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial07_dependencies.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/8 14:56
@copyright Copyright (c) 2026/9/8 WeiLi
@Description:

# script command: uvicorn tutorial07_dependencies:app --reload
"""

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select, delete, update
from models.user import User
from models import AsyncFactory, AsyncSession
from typing import List


# -------- async session object
async def get_session():
    session = AsyncFactory()
    try:
        yield session
    finally:
        await session.close()


# --------------------------------
# Schema for Pydantic model
class UserSchemaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    username: str
    mobile: str


# --------------------------------
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user/add", response_model=UserSchemaOut)
async def add_user(session: AsyncSession = Depends(get_session)):
    # 开启事物
    async with session.begin():
        user = User(email="weili_ithaca@126.com", username="Ithaca", password="123456", mobile="123123")
        session.add(user)
    return user


# -------- CRUD 增删查改操作
@app.get("/user/select/{user_id}", response_model=UserSchemaOut)
async def select_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar()
        if user is None:
            raise HTTPException(status_code=404, detail=f"User id={user_id} 不存在")
        return user


@app.get("/user/select", response_model=List[UserSchemaOut])
async def get_user(session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = select(User).where(User.email.contains("weili"))
        result = await session.execute(stmt)
        users = result.scalars().all()  # 转成 list，而不是返回 ScalarResult 游标
        return users


@app.delete("/user/delete/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = delete(User).where(User.id == user_id)
        await session.execute(stmt)
        return {"message": "OK"}


@app.put("/user/update/{user_id}")
async def update_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        stmt = update(User).where(User.id == user_id).values(password=8208208820)
        await session.execute(stmt)
        return {"message": "update data OK"}


@app.put("/user/update_get/{user_id}", response_model=UserSchemaOut)
async def update_get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        # 先查找 后修改
        user = await session.scalar(select(User).where(User.id == user_id))
        user.password = 8208208820
        return user

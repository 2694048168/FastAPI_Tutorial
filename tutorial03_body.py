#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial03_body.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 11:53
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

# script command: uvicorn tutorial03_body:app --reload
from fastapi import FastAPI, Path
from pydantic import BaseModel, Field
from typing import Annotated

# create FastAPI instance
app = FastAPI()


# 通过Python装饰器功能: FastAPI instance  ---> 请求方法 ---> 请求路径
@app.get("/")
# 异步执行 ---> URL路由请求与处理函数(响应结果)
async def root():
    return {"message": "Hello World for root path"}


# path传参
@app.get("/p/article/{article_id}")
async def article_detail(article_id: Annotated[int, Path] = Path(..., ge=1)):
    return {"message": f"the article id = {article_id}"}


class LoginInfo(BaseModel):
    # Field 的第一个参数 ... 表示该参数是必须的，不能省略(不能为空)，非可选的
    email: Annotated[str, Field(..., description="邮箱", min_length=1, max_length=50)]
    password: Annotated[str, Field(min_length=6, max_length=20, description="密码")]


@app.post("/login")
async def login(data: LoginInfo):
    return {f"the login info: email = {data.email}, password: {data.password}"}

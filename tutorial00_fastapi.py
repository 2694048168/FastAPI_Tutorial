#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial00_fastapi.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 11:14
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: uv add fastapi uvicorn
"""

# https://fastapi.tiangolo.com/
# script command: uvicorn tutorial00_fastapi:app --reload
from fastapi import FastAPI

# create FastAPI instance
app = FastAPI()


# 通过Python装饰器功能: FastAPI instance  ---> 请求方法 ---> 请求路径
@app.get("/")
# 异步执行 ---> URL路由请求与处理函数(响应结果)
async def root():
    return {"message": "Hello World for root path"}


@app.get("/hello/{name}")
async def get_hello(name: str):
    return {"message": f"Hello {name}, welcome the first FastAPI tutorial"}

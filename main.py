#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: main.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/4 16:59
@copyright Copyright (c) 2026/9/4 WeiLi
@Description: uv add fastapi uvicorn
"""

# script command: uvicorn main:app --reload
from fastapi import FastAPI
from fastapi import Path, Query


# create FastAPI instance
app = FastAPI()

# 通过Python装饰器功能: FastAPI instance  ---> 请求方法 ---> 请求路径
@app.get("/")
# 异步执行 ---> URL路由请求与处理函数(响应结果)
async def root():
    return {"message": "Hello World for root path"}

@app.get("/hello")
async def get_hello():
    return {"message": "Hello FastAPI first tutorial"}

# 路径参数, URL的一部分, 资源的唯一定位符
@app.get("/hello/{name}")
async def get_name(name : str):
    return {"message": f"Hello {name}, this is your first FastAPI"}

@app.get("/hello_id/{id}")
async def get_id(id : int):
    return {f"hell id={id}, this is your {id} FastAPI"}

# 路径参数 Python原生类型注解 + FastAPI Path 类型注解
@app.get("/book_id/{id}")
async def get_book_id(id : int = Path(..., gt=0, lt=101, desc="book id range")):
    return {f"这是第 {id} 书籍"}

# 查询参数 Python原生类型注解 + FastAPI Query 类型注解
@app.get("/new/new_list")
async def get_new(skip : int = Query(0, lt=100, description="跳过的记录数"),
                  limit: int = Query(10, description="返回的记录数")):
    return {f"this skip value = {skip}, and the limit value = {limit}"}

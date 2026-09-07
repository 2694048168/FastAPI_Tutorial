#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial02_param.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 11:38
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

# script command: uvicorn tutorial02_param:app --reload
from fastapi import FastAPI, Path, Query
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
# async def article_detail(article_id: int):
# async def article_detail(article_id: int=Path(ge=2):
async def article_detail(article_id: Annotated[int, Path] = Path(..., ge=1)):
    return {"message": f"the article id = {article_id}"}


# 查询传参
# http://127.0.0.1:8000/article/list?page=2&per_page=10
@app.get("/article/list")
# async def article_list(page: int = 0, per_page: int = 10):
async def article_list(page: Annotated[int, Query(ge=1)] = 1,
                       per_page: Annotated[int, Query(ge=10)] = 10):
    return {"message": f"the page = {page}, per_page = {per_page}"}

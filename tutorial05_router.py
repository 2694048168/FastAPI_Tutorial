#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial05_router.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 12:20
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: API Router
"""

# script command: uvicorn tutorial05_router:app --reload
from fastapi import FastAPI
from routers.user import router as UserRouter
from routers.article import router as ArticleRouter

app = FastAPI()
# APIRouter 添加
app.include_router(UserRouter)
app.include_router(ArticleRouter)

@app.get("/")
async def root():
    return {"message": "Hello World for root path"}

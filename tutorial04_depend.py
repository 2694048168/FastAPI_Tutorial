#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial04_depend.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 12:03
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 依赖注入，在需要的视图函数中注入该功能函数依赖
1. 共享业务逻辑 复用
2. 共享数据库连接
3. 实现安全、验证、角色权限
4. 日志记录
"""

# script command: uvicorn tutorial04_depend:app --reload
from fastapi import FastAPI, Depends
from typing import Dict

app = FastAPI()


async def page_common(skip: int = 0, limit: int = 10):
    return {"page": skip, "limit": limit}


@app.get("/user/list")
async def get_page_list(page_param: Dict = Depends(page_common)):
    page = page_param.get('skip')
    size = page_param.get('limit')
    return {f"page :{page}, limit:{size}"}


@app.get("/movie/list")
async def get_page_list(page_param: Dict = Depends(page_common)):
    return {f"page :{page_param.get('skip')}, limit:{page_param.get('limit')}"}

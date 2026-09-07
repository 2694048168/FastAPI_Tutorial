#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: user.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:09
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

# /user/list
@router.get("/list")
async def user_list():
    return {"users": ["张三", "李四"]}

# /usesr/123
@router.get("/{user_id}")
async def user_detail(user_id: int):
    return {"user_id": user_id}

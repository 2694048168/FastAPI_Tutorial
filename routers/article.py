#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: article.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 14:09
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: 
"""

from fastapi import APIRouter

router = APIRouter(prefix="/article", tags=["article"])


# /article/list
@router.get("/list")
async def article_list():
    return {"articles": ["体育", "经济"]}


# /article/123
@router.get("/{article_id}")
async def article_detail(article_id: int):
    return {"article_id": article_id}

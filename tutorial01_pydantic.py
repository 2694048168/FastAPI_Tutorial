#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial01_pydantic.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/7 11:17
@copyright Copyright (c) 2026/9/7 WeiLi
@Description: https://pydantic.dev/docs/validation/latest/get-started/
"""

from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    # date | None === Optional[date]
    date_joined: Optional[date]
    department: List[str] | None


external_data = {
    "id": 42,
    "name": "Ithaca",
    "date_joined": date(2027, 3, 17),
    "department": ["技术部", "产品部", "研发部"],
}

user = User(**external_data)
print(f"user id: {user.id} and name: {user.name}")
# convert into dict.
print(user.model_dump())

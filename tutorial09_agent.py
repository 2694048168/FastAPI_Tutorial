#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File: tutorial09_agent.py
@Author: WeiLi
@Email: weili_yzzcq@163.com
@Blog: https://2694048168.github.io/blog/
@Date: 2026/9/14 15:59
@copyright Copyright (c) 2026/9/14 WeiLi
@Description:

pip install langchain
pip install langchain-deepseek

uv add langchain
uv add langchain-deepseek
"""
from openai.types import image_input_reference_param
from pydantic import BaseModel, Field, SecretStr
from typing import Annotated, List, Literal
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
import asyncio


# --------- 保证大模型的输出内容格式符合需求，创建数据结构 Schema
class NameSchema(BaseModel):
    name: Annotated[str, Field(..., description="姓名")]
    reference: Annotated[str, Field(..., description="出处")]
    moral: Annotated[str, Field(..., description="寓意")]


class NameResultSchema(BaseModel):
    names: List[NameSchema]


# --------- 校验生成结果，保证前端上传数据的合法性,生成结果返回数据的格式
# 创建 NameIn 和 NameOut Schema
class NameIn(BaseModel):
    surname: Annotated[str, Field(..., description="姓氏")]
    gender: Annotated[Literal["不限", "女", "男"], Field(..., description="性别")]
    length: Annotated[Literal["不限", "单字", "双字"], Field(..., description="字数")]
    other: Annotated[str | None, Field("", description="其他要求")]
    exclude: Annotated[List[str], Field([], description="排除的名字")]


class NameOut(BaseModel):
    names: List[NameSchema]


# --------- Agent core code
llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=SecretStr("deepseek-API-key"),
    temperature=1
)

system_prompt = """
你是一位精通汉语言文学、音韵学和传统文化的命名专家，擅长为人物创作兼具音律美感、深刻蕴意的与文化内涵的姓名。
请严格遵循以下原则进行命名：

1. 发音优先：名字需平仄协调，声调起伏自然，避免拗口，谐音歧义(如不雅谐音、负面联想)，朗朗上口，富有韵律感;
2. 寓意深远：结合用户提供的背景(如姓氏、性别、字数和其他要求等)，选取具有积极象征意义的意象(如自然元素、美德品质、
经典典故)，做到"名以载道"；
3. 内涵厚重：优先从《诗经》、《楚辞》、《论语》等经典文献，或唐诗宋词、成语典故中汲取灵感，确保名字有出处、有底蕴，
避免空洞堆砌；
4. 现代适配：在尊重传统的基础上兼顾当代语语境与审美，避免过度古傲或生僻字，
生僻字需附注，附注音与释义，确保适用性与传播性；
5. 个性化定制：根据用户具体的需求（如性别倾向、字数限制、风格偏好、儒雅清丽、大方灵动等)，提供5个候选方案，
并按照以下格式输出:
【姓名】姓名
【出处】典籍来源或文化意象
【寓意】字义拆解或整体象征
"""

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    response_format=NameResultSchema
)


async def generate_name(name_info: NameIn) -> NameResultSchema:
    prompt = (f"用户姓氏是：{name_info.surname}, 性别是：{name_info.gender}, 名字字数要求是：{name_info.length}，"
              f"其他要求是：{name_info.other}，排除的名字有：{"、".join(name_info.exclude)}")
    result = await agent.ainvoke({
        "messages": [{'role': 'user', 'content': prompt}]
    })
    print(result)
    return result["structured_response"]


async def main():
    name_info = NameIn(
        surname='周',
        gender='女',
        length='双字'
    )

    names = await generate_name(name_info)
    print("----------------------------------")
    print(names)


# ---------------------
if __name__ == '__main__':
    asyncio.run(main())

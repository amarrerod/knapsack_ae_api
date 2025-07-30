#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   decode.py
@Time    :   2025/07/30 11:02:33
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
'''

from app.models import KP
from app.transformers import decode, encode
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

router = APIRouter()

@router.get("/decode")
async def decode_instance(x0: float, x1: float) -> JSONResponse:
    instance = await decode(x0, x1)
    return JSONResponse(content=jsonable_encoder(instance))


@router.post("/encode")
async def encode_instance(instance: KP):
    """Encodes a Knapsack Instance into a 2D vector

    Args:
        instance (KP): Knapsack Model

    Returns:
        JSONResponse: Where content is tuple with the values (x0, x1)
    """
    encoding = await encode(instance)
    return JSONResponse(content=(encoding))

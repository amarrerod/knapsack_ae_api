#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2025/07/30 10:56:05
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
'''


from ._autoencoder import __decode_instances, __encode_instances
from app.models import KP, read_instance

async def decode(x0: float, x1: float):
    variables = __decode_instances((x0, x1))
    return KP(size=len(variables), variables=variables)

async def encode(instance: KP):
    return (__encode_instances(instance.variables), 200)

async def encode_from_path(path: str):
    try:
        return (__encode_instances(read_instance(path).variables), 200)
    except FileNotFoundError as f:
        print(f"File: {path} not found. Error f: {f.errno}")
        return ((None, None), f.errno)
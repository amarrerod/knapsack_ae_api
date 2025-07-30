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
import numpy as np

async def decode(x0: float, x1: float):
    variables = __decode_instances(np.asarray([x0, x1]).reshape(1, -1))
    return KP(size=(len((variables // 2) - 1)), variables=variables)

async def encode(instance: KP):
    return (__encode_instances(np.asarray(instance.variables).reshape(1, -1)), 200)

async def encode_from_path(path: str):
    try:
        return (__encode_instances(np.asarray(read_instance(path).variables).reshape(1, -1)), 200)
    except FileNotFoundError as f:
        print(f"File: {path} not found. Error f: {f.errno}")
        return ((None, None), f.errno)
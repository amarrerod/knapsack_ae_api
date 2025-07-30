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
from app.models import KP
import numpy as np

async def decode(x0: float, x1: float):
    variables = __decode_instances(np.asarray([x0, x1]).reshape(1, -1))
    print(len(variables), variables)
    return KP(size=(len((variables // 2) - 1)), variables=variables)

async def encode(instance: KP):
    return  __encode_instances(np.asarray(instance.variables).reshape(1, -1))

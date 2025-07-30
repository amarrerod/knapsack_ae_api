#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   kp.py
@Time    :   2025/07/30 10:55:10
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
'''

from pydantic import BaseModel
from typing import Optional


class KP(BaseModel):
    size: int = 0
    variables: Optional[list[int]] = None

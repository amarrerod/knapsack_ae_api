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
import numpy as np

class KP(BaseModel):
    """Knapsack Instance Model

        - size (int): Number of variables of the instance. It's defined as 2N+1 since
            the instance contains N pairs of weights and profirts (w_i, p_i) plus the capacity (Q)
        - variables (list[int]): Variables of the instance
    """
    size: int = 0
    variables: list[int]

class KPCollection(BaseModel):
    instances: list[KP] = list()

def read_instance(path: str) -> KP:
    """Reads and instance from the file system

    Args:
        path (str): Path where the instance is stored

    Returns:
        KP: Returns a KP object
    """
    content = np.loadtxt(path, dtype=int)
    variables = [content[0][1], *content[1:].flatten()]
    return KP(size=(content[0][0] * 2)+ 1, variables=variables)


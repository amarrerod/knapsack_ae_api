#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   decode.py
@Time    :   2025/07/30 11:02:33
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from app.models import KP
from app.transformers import decode, encode, encode_from_path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/decode")
async def decode_instance(
    x0: float = Query(..., description="First coordinate (x0)"),
    x1: float = Query(..., description="Second coordinate (x1)"),
) -> JSONResponse:
    """Reconstructs a Knapsack Instance from a 2D vector
    

    Args:
        - x0 (float): First coordinate
        - x1 (float): Second coordinate

    Returns:
        JSONResponse: Knapsack instance
    """
    instance = await decode(x0, x1)
    if any(x < 0 for x in instance.variables):
        return JSONResponse(
            status_code=406,
            content={
                "error": f"Instance with encoding ({x0}, {x1}) does not exists in the space.Encoder predicted negative profits or weights",
                "instance": jsonable_encoder(instance),
            },
        )
    if instance.size // 2 == 0:
        return JSONResponse(
            status_code=406,
            content={
                "error": f"""Instance with encoding ({x0}, {x1}) does not exists in the space, odd number of variables found. 
                            Note that a KP instance must have a even number of variables. In particular, 2N (weights and profits) plus capacity (Q)."""
            },
        )
    return JSONResponse(
        content={"encoding": (x0, x1), "instance": jsonable_encoder(instance)}
    )


@router.post("/encode")
async def encode_instance(instance: KP):
    """Encodes a Knapsack Instance into a 2D vector

    Args:
        instance (KP): Knapsack Model

    Returns:
        JSONResponse: Where content is tuple with the values (x0, x1)
    """
    encoding, status = await encode(instance)
    return JSONResponse(content={"instance": instance, "encoding": encoding})


@router.get("/encode/filename")
async def encode_from_file(path: str):
    """Encodes a Knapsack Instance into a 2D vector
    from a filename in the machine

    Args:
        path (str): Filename to read the instance

    Returns:
        JSONResponse: Where content is tuple with the values (x0, x1)
    """
    encoding, status = await encode_from_path(path)
    if status != 200:
        return JSONResponse(
            status_code=400,
            content={
                "error": f"Bad Request. Filename: {path} not found in the directory"
            },
        )
    return JSONResponse(content={"instance": path, "encoding": encoding})


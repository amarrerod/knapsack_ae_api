#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   _autoencoder.py
@Time    :   2025/07/30 11:10:23
@Author  :   Alejandro Marrero 
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
'''

import joblib
import keras
from pathlib import Path
import numpy as np

SCALER_FN = Path(__file__).with_name("N_variable_scaler.sav")
ENCODER = Path(__file__).with_name("best_kp_AE_N_variable_2D_tuned_encoder.keras")
DECODER = Path(__file__).with_name("best_kp_AE_N_variable_2D_tuned_decoder.keras")
MAXLEN = 2001

def __encode_instances(X: list[int]):
    _X = np.asarray(X)
    if len(_X) < MAXLEN:
        _X = np.pad(_X, (0, MAXLEN - len(_X)), "constant")
    _X = _X.reshape(1, -1)
    scaler = joblib.load(SCALER_FN)
    encoder = keras.models.load_model(ENCODER)
    x, y = encoder(scaler.transform(_X))[0]
    return (float(x), float(y))

def __decode_instances(X : tuple[float, float]):
    _X = np.asarray(X).reshape(1, -1)
    scaler = joblib.load(SCALER_FN)
    decoder = keras.models.load_model(DECODER)
    variables =  scaler.inverse_transform(decoder(_X))[0]
    idx = np.argmin((variables[1:]<0) == False) + 1
    return variables[:idx].astype(np.int32)
    


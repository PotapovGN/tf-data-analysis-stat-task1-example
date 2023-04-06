import pandas as pd
import numpy as np


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = (2 * x) / 9
    return y.mean()


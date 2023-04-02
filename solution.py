import pandas as pd
import numpy as np


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    
    n = len(x)
    a = (1/n) * np.sum(x / (1.5 ** 2))
    return a


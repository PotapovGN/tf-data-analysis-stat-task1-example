import pandas as pd
import numpy as np


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    
    loc = np.median(x)
    scale = np.mean(np.abs(x - loc))
    
    acceleration = 2 / (scale ** 2)
    
    return acceleration

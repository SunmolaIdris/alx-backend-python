#!/usr/bin/env python3
'''Task 8's solution.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier

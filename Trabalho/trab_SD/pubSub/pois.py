import math
import random

def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

def PoisTime(n_events,time_interval):
    return nextTime(n_events/time_interval)
from SimulatedAnnealing import *


def first_method(t0, alpha, k):
    return t0 * (alpha ** k)

def second_method(t0, alpha, k):
    return (t0)/(1+alpha*(math.log(1+k, 10)))

def third_method(t0, alpha, k):
    return (t0)/(1+alpha*k)

def fourth_method( t0, alpha, k):
    return (t0)*(1+ alpha * (k**2))    

s = SimulatedAnnealing()
s.simulated_annealing(second_method, 200000)
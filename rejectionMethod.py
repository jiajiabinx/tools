from random import *
import numpy as np
import matplotlib.pyplot as plt

__all__ = ["f", "pdfrandgen","PlotnTrials"]


def f(x):
    """
    default function
    """
    return 6*x**2*(1-x)**2

def pdfrandgen(pdf = f,x1=-1,x2=1):
    """
    generate a pseudo random number with a certain pdf and range [x1,x2]
    """
    M = 24
    while True:
        T = np.random.uniform(x1,x2)
        U = np.random.uniform(0,1)
        while (24*U > pdf(T)):
            T = np.random.uniform(x1,x2)
            U = np.random.uniform(0,1)
        yield T

def PlotnTrials(n = 100000):
    g = pdfrandgen()
    y = [next(g) for _ in range(n)]
    x1 = np.arange(-1,1,0.002)
    x2 = np.arange(-1,1,2/n)
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(x1,f(x1),"b")
    plt.subplot(2,1,2)
    plt.plot(x2, y ,"k")
    plt.show()

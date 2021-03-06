#! /usr/bin/python3
import numpy as np

# Transformación de Clarke : ABC a Alpha-Beta-0
def abc_to_alphaBeta0(a, b, c):
    alpha = (2/3)*(a - b/2 - c/2)
    beta  = (2/3)*(np.sqrt(3)*(b-c)/2)
    z     = (2/3)*((a+b+c)/2)
    return alpha, beta, z

# Inversa Transformación de Clarke : alphaBeta0 a abc
def alphaBeta0_to_abc(alpha, beta, z):
    a = alpha + z
    b = -alpha/2 + beta*np.sqrt(3)/2 + z
    c = -alpha/2 - beta*np.sqrt(3)/2 + z
    return a, b, c

# Transformación de Park: abc a dq0
def abc_to_dq0(a, b, c, wt, delta):
  d = (2/3)*(a*np.sin(wt+delta) + b*np.sin(wt+delta-(2*np.pi/3)) + c*np.sin(wt+delta+(2*np.pi/3)))
  q = (2/3)*(a*np.cos(wt+delta) + b*np.cos(wt+delta-(2*np.pi/3)) + c*np.cos(wt+delta+(2*np.pi/3)))
  z = (2/3)*(a+b+c)/2
  return d, q, z

# Inversa de Transformación de Park
def dq0_to_abc(d, q, z, wt, delta):
    a = d*np.sin(wt+delta) + q*np.cos(wt+delta) + z
    b = d*np.sin(wt-(2*np.pi/3)+delta) + q*np.cos(wt-(2*np.pi/3)+delta) + z
    c = d*np.sin(wt+(2*np.pi/3)+delta) + q*np.cos(wt+(2*np.pi/3)+delta) + z
    return a, b, c

# Transformación Clarke a Park
def alphaBeta0_to_dq0(alpha, beta, zero, wt, delta):
    d = alpha*np.sin(wt+delta) - beta*np.cos(wt+delta)
    q = alpha*np.cos(wt+delta) + beta*np.sin(wt+delta)
    z = zero
    return d, q, z

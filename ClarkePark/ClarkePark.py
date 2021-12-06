#! /usr/bin/python3
import numpy as np

def version():
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("                                                                          ")
    print("                         ─▄▀─▄▀")
    print("                         ──▀──▀")
    print("                         █▀▀▀▀▀█▄")
    print("                         █░░░░░█─█")
    print("                         ▀▄▄▄▄▄▀▀")
    print("                                                                          ")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("| Packages : ClarkePark                                                  |")
    print("| Fecha : 06/12/2021                                                     |")
    print("| Version : 0.1.6                                                        |")
    print("| Autor : Marco Polo Jacome Toss                                         |")
    print("| License: GNU Affero General Public License v3 (GPL-3.0)                |")
    print("| Requires: Python >=3.5                                                 |")
    print("| PyPi : https://pypi.org/project/ClarkePark/                            |")
    print("| Donativos : https://ko-fi.com/jacometoss                               |")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
# Transformación de Clarke : ABC a Alpha-Beta-0
def abc_to_alphaBeta0(a, b, c):
    '''
    ABC --> αβ
    ----------------
    Transformation of time components, frame A, B, C to new axes
    of reference stationary orthogonal α, β.
    
    Instructions
    -------------
    Enter the three-phase signals in the order shown
    
    abc_to_alphaBeta0(a, b, c)

    You require Numpy and as an example of these signals

    end_time = 10/float(60)
    step_size = end_time/(1000)
    t = np.arange(0,end_time,step_size)
    wt = 2*np.pi*float(60)*t
    delta = 0    
    
    A = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
    B = (np.sqrt(2)*float(127))*np.sin(wt+rad_angB)
    C = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)

    The data is transformed with

    alpha = (2/3)*(a - b/2 - c/2)
    beta  = (2/3)*(np.sqrt(3)*(b-c)/2)
    z     = (2/3)*((a+b+c)/2)    
    
    '''
    alpha = (2/3)*(a - b/2 - c/2)
    beta  = (2/3)*(np.sqrt(3)*(b-c)/2)
    z     = (2/3)*((a+b+c)/2)
    return alpha, beta, z

# Inversa Transformación de Clarke : alphaBeta0 a abc
def alphaBeta0_to_abc(alpha, beta, z):

    '''
    αβ --> ABC
    ----------------
    Clarke's inverse, orthogonal stationary reference
    axes α, β to time domain components, frame A, B, C.
    
    Instructions
    -------------
    Enter the three-phase signals in the order shown
    
    alphaBeta0_to_abc(alpha, beta, z)

    You require Numpy and as an example of these signals

    The data is transformed with

    a = alpha + z
    b = -alpha/2 + beta*np.sqrt(3)/2 + z
    c = -alpha/2 - beta*np.sqrt(3)/2 + z 
    
    '''    
    a = alpha + z
    b = -alpha/2 + beta*np.sqrt(3)/2 + z
    c = -alpha/2 - beta*np.sqrt(3)/2 + z
    return a, b, c

# Transformación de Park: abc a dq0
def abc_to_dq0(a, b, c, wt, delta):
    '''
    ABC --> dq0
    ----------------
    Transformation of time components, ABC frame towards
    a permanent dq0 reference system.
    
    Instructions
    -------------
    Enter the three-phase signals in the order shown
    
    abc_to_dq0(a, b, c, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    d = (2/3)*(a*np.sin(wt+delta) + b*np.sin(wt+delta-(2*np.pi/3)) + c*np.sin(wt+delta+(2*np.pi/3)))
    q = (2/3)*(a*np.cos(wt+delta) + b*np.cos(wt+delta-(2*np.pi/3)) + c*np.cos(wt+delta+(2*np.pi/3)))
    z = (2/3)*(a+b+c)/2

    '''
    d = (2/3)*(a*np.sin(wt+delta) + b*np.sin(wt+delta-(2*np.pi/3)) + c*np.sin(wt+delta+(2*np.pi/3)))
    q = (2/3)*(a*np.cos(wt+delta) + b*np.cos(wt+delta-(2*np.pi/3)) + c*np.cos(wt+delta+(2*np.pi/3)))
    z = (2/3)*(a+b+c)/2
    return d, q, z

# Inversa de Transformación de Park
def dq0_to_abc(d, q, z, wt, delta):
    '''
    dq0 --> ABC
    ----------------
    Park's inverse, rotary reference axes dq0
    to time domain components, frame A, B, C.
    
    Instructions
    -------------
    Enter the three-phase signals in the order shown
    
    dq0_to_abc(d, q, z, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    a = d*np.sin(wt+delta) + q*np.cos(wt+delta) + z
    b = d*np.sin(wt-(2*np.pi/3)+delta) + q*np.cos(wt-(2*np.pi/3)+delta) + z
    c = d*np.sin(wt+(2*np.pi/3)+delta) + q*np.cos(wt+(2*np.pi/3)+delta) + z

    ''' 
    a = d*np.sin(wt+delta) + q*np.cos(wt+delta) + z
    b = d*np.sin(wt-(2*np.pi/3)+delta) + q*np.cos(wt-(2*np.pi/3)+delta) + z
    c = d*np.sin(wt+(2*np.pi/3)+delta) + q*np.cos(wt+(2*np.pi/3)+delta) + z
    return a, b, c

# Transformación Clarke a Park
def alphaBeta0_to_dq0(alpha, beta, zero, wt, delta):
    '''
    αβ --> dq0 
    ----------------
    Orthogonal stationary reference transformation α, β
    towards a rotating reference frame dq0.
    
    Instructions
    -------------
    Enter the three-phase signals in the order shown
    
    alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    d = alpha*np.sin(wt+delta) - beta*np.cos(wt+delta)
    q = alpha*np.cos(wt+delta) + beta*np.sin(wt+delta)
    z = zero

    '''     
    d = alpha*np.sin(wt+delta) - beta*np.cos(wt+delta)
    q = alpha*np.cos(wt+delta) + beta*np.sin(wt+delta)
    z = zero
    return d, q, z

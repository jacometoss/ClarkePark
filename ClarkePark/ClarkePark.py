#! /usr/bin/python3
import numpy as np
import numpy.typing as npt


# Will return plenty of 3-tuples of numpy arrays, so creating alias
try:
    three_arrays = tuple[npt.NDArray, npt.NDArray, npt.NDArray]
except TypeError:
    # Only acceptable syntax for Python >=3.9
    from typing import Tuple
    three_arrays = Tuple[npt.NDArray, npt.NDArray, npt.NDArray]


def version():
    print(74*":")
    print(74*" ")
    print("                         ─▄▀─▄▀")
    print("                         ──▀──▀")
    print("                         █▀▀▀▀▀█▄")
    print("                         █░░░░░█─█")
    print("                         ▀▄▄▄▄▄▀▀")
    print(74*" ")
    print(74*":")
    print(f"{'| Packages : ClarkePark': <73}|")
    print(f"{'| Fecha : 10/01/2022': <73}|")
    print(f"{'| Version : 0.1.7': <73}|")
    print(f"{'| Autor : Marco Polo Jacome Toss': <73}|")
    print(f"{'| License: GNU Affero General Public License v3 (GPL-3.0)': <73}|")  # noqa: E501
    print(f"{'| Requires: Python >=3.5': <73}|")
    print(f"{'| PyPi : https://pypi.org/project/ClarkePark/': <73}|")
    print(f"{'| Donativos : https://ko-fi.com/jacometoss': <73}|")
    print(74*":")


# Define Clarke transformation matrix
T_clarke = (2/3)*np.array([[1, -0.5, -0.5],
                           [0, np.sqrt(3)/2, -np.sqrt(3)/2],
                           [0.5, 0.5, 0.5]])

# Define inverse Clarke tranformation matrix
T_clarke_inv = np.linalg.inv(T_clarke)


# Transformación de Clarke : ABC a Alpha-Beta-0
def abc_to_alphaBeta0(a: npt.ArrayLike, b: npt.ArrayLike,
                      c: npt.ArrayLike) -> three_arrays:
    '''
    ABC --> αβ
    ----------------
    Transformation of time components, frame A, B, C to new axes
    of reference stationary orthogonal α, β.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    alpha, beta, z = abc_to_alphaBeta0(a, b, c)

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
    input = np.array([a, b, c])
    alpha, beta, z = T_clarke @ input
    return alpha, beta, z


# Inversa Transformación de Clarke : alphaBeta0 a abc
def alphaBeta0_to_abc(alpha: npt.ArrayLike, beta: npt.ArrayLike,
                      z: npt.ArrayLike) -> three_arrays:
    '''
    αβ --> ABC
    ----------------
    Clarke's inverse, orthogonal stationary reference
    axes α, β to time domain components, frame A, B, C.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    a, b, c = alphaBeta0_to_abc(alpha, beta, z)

    You require Numpy and as an example of these signals

    The data is transformed with

    a = alpha + z
    b = -alpha/2 + beta*np.sqrt(3)/2 + z
    c = -alpha/2 - beta*np.sqrt(3)/2 + z

    '''
    a, b, c = T_clarke_inv @ np.array([alpha, beta, z])
    return a, b, c


# Define transformation matrix for Park Transform
def park_matrix(wt: npt.ArrayLike, delta: float) -> npt.NDArray[np.float64]:
    '''
    Transformation Matrix describing ABC --> dq0
     ----------------
    Defines transformation Matrix for Park Transformation of time
    components, ABC frame towards a permanent dq0 reference system.

    Instructions
    -------------
    Just need to enter properties of the (rotating) reference frame, namely:

        wt      - Array describing how the reference frame
                  is rotating (wt - angular frequency).

        delta   - Float describing initial phase angle
    '''
    # Create Park transformation tensor
    sin_0 = np.sin(wt + delta)
    sin_p = np.sin(wt + delta + 2*np.pi/3)
    sin_n = np.sin(wt + delta - 2*np.pi/3)
    cos_0 = np.cos(wt + delta)
    cos_p = np.cos(wt + delta + 2*np.pi/3)
    cos_n = np.cos(wt + delta - 2*np.pi/3)
    half = 0.5 * np.ones(len(wt))

    P = np.array([[sin_0, sin_n, sin_p],
                  [cos_0, cos_n, cos_p],
                  [half,  half,  half]])

    P *= (2/3)
    return P


# Transformación de Park: abc a dq0
def abc_to_dq0(a: npt.ArrayLike, b: npt.ArrayLike, c: npt.ArrayLike,
               wt: npt.ArrayLike, delta: float) -> three_arrays:
    '''
    ABC --> dq0
    ----------------
    Transformation of time components, ABC frame towards
    a permanent dq0 reference system.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    d, q, z = abc_to_dq0(a, b, c, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    d = (2/3)*(a*np.sin(wt+delta) +
        b*np.sin(wt+delta-(2*np.pi/3)) +
        c*np.sin(wt+delta+(2*np.pi/3)))

    q = (2/3)*(a*np.cos(wt+delta) +
        b*np.cos(wt+delta-(2*np.pi/3)) +
        c*np.cos(wt+delta+(2*np.pi/3)))

    z = (2/3)*(a+b+c)/2

    '''
    # Turn all three inputs into a vector
    vec = np.array([a, b, c])

    # Get Park transformation matrix
    park = park_matrix(wt, delta)

    # Use Einstein notation to define tensor operation
    # (inner product repeated over time axis)
    d, q, z = np.einsum('ij..., j... -> i...', park, vec)

    return d, q, z


# Inversa de Transformación de Park
def dq0_to_abc(d: npt.ArrayLike, q: npt.ArrayLike, z: npt.ArrayLike,
               wt: npt.ArrayLike, delta: float) -> three_arrays:
    '''
    dq0 --> ABC
    ----------------
    Park's inverse, rotary reference axes dq0
    to time domain components, frame A, B, C.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    a, b, c = dq0_to_abc(d, q, z, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    a = d*np.sin(wt+delta) + q*np.cos(wt+delta) + z
    b = d*np.sin(wt-(2*np.pi/3)+delta) + q*np.cos(wt-(2*np.pi/3)+delta) + z
    c = d*np.sin(wt+(2*np.pi/3)+delta) + q*np.cos(wt+(2*np.pi/3)+delta) + z

    '''
    # Turn all three inputs into a vector
    vec = np.array([d, q, z])

    # Get Park transformation matrix and calculate inverse
    park = park_matrix(wt, delta)
    park_inv = np.linalg.inv(park.T).T

    # Use Einstein notation to define tensor operation
    # (inner product repeated over time axis)
    a, b, c = np.einsum('ij..., j... -> i...', park_inv, vec)
    return a, b, c


# Transformación Clarke a Park
def alphaBeta0_to_dq0(alpha: npt.ArrayLike, beta: npt.ArrayLike,
                      zero: npt.ArrayLike, wt: npt.ArrayLike,
                      delta: float) -> three_arrays:
    '''
    αβ --> dq0
    ----------------
    Orthogonal stationary reference transformation α, β
    towards a rotating reference frame dq0.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    d, q, z = alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)

    You require Numpy and as an example of these signals

    The data is transformed with

    d = alpha*np.sin(wt+delta) - beta*np.cos(wt+delta)
    q = alpha*np.cos(wt+delta) + beta*np.sin(wt+delta)
    z = zero

    '''
    # Calculate Park transformation matrix
    P = park_matrix(wt, delta)

    # Create vector of αβ0 and apply transformation
    # Transform: αβ -> Inverse Clarke -> Park -> dq0
    vec = np.array([alpha, beta, zero])
    d, q, z = P @ T_clarke_inv @ vec

    return d, q, z


# Transformación Park a Clarke
def dq0_to_alphaBeta0(d: npt.ArrayLike, q: npt.ArrayLike, z: npt.ArrayLike,
                      wt: npt.ArrayLike, delta: float) -> three_arrays:
    '''
    dq0 --> αβ
    ----------------
    rotating reference frame dq0 towards an
    orthogonal stationary reference transformation α, β.

    Instructions
    -------------
    Enter the three-phase signals in the order shown

    alpha, beta, zero = dq0_to_alphaBeta0(d, q, z, wt, delta)
    '''
    # Calculate Park transformation matrix and its inverse
    P = park_matrix(wt, delta)
    park_inv = np.linalg.inv(P.T).T

    # Create vector of αβ0 and apply transformation
    # Transform: dq0 -> Inverse Park -> Clarke -> αβ
    vec = np.array([d, q, z])
    alpha, beta, zero = T_clarke @ park_inv @ vec

    return alpha, beta, zero

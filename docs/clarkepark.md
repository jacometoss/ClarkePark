[![PyPI version](https://badge.fury.io/py/ClarkePark.svg)](https://badge.fury.io/py/ClarkePark)
[![versons of python supported by carsons](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ClarkePark/)
[![Downloads](https://pepy.tech/badge/clarkepark)](https://pepy.tech/project/clarkepark)
[![Downloads](https://pepy.tech/badge/clarkepark/month)](https://pepy.tech/project/clarkepark)
[![Maintainability](https://api.codeclimate.com/v1/badges/6abceb2a140780c13d17/maintainability)](https://codeclimate.com/github/jacometoss/ClarkePark/maintainability)

# Marcos de referencia de una señal trifásica balanceada

Para poder usar la transformación es necesario generar las tres señales monofásicas en desfase y balanceadas siendo necesario de 

- *Numpy* : Para el manejo de los datos.
- *Matplotlib* : Obtener las gráficas correspondientes.

```python
import ClarkePark
import numpy as np
import matplotlib.pyplot as plt

end_time = 10/float(60)
step_size = end_time/(1000)
t = np.arange(0,end_time,step_size)
wt = 2*np.pi*float(60)*t
delta = 0

rad_angA = float(0)*np.pi/180
rad_angB = float(240)*np.pi/180
rad_angC = float(120)*np.pi/180

A = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
B = (np.sqrt(2)*float(127))*np.sin(wt+rad_angB)
C = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)

alpha, beta, z = ClarkePark.abc_to_alphaBeta0(A,B,C)
d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)

# Plot ABC
plt.figure(figsize=(8,3))
plt.plot(t, A, label="A", color='k')
plt.plot(t, B, label="B", color='darkred')
plt.plot(t, C, label="C", color="darkblue")
plt.legend(['A','B','C'])
plt.legend(ncol=3,loc=4)
plt.ylabel("Tensión [Volts]")
plt.xlabel("Tiempo [Segundos]")
plt.title(" Tensión trifásica (ABC)")
plt.grid('on')
plt.show()

# Plot Alfa-Beta
plt.figure(figsize=(8,3))
plt.plot(t, alpha, label="\u03B1", color="darkred")
plt.plot(t, beta, label="\u03B2", color="darkblue")
plt.plot(t, z, label="zero" , color="dimgray")
plt.legend(['\u03B1','\u03B2','0'])
plt.legend(ncol=3,loc=4)
plt.ylabel("Tensión [Volts]")
plt.xlabel("Tiempo [Segundos]")
plt.title(" Transformación Clarke (\u03B1 \u03B2)")
plt.grid('on')
plt.show()

# Plot DQ0
plt.figure(figsize=(8,3))
plt.plot(t, d, label="d", color="royalblue")
plt.plot(t, q, label="q", color="orangered")
plt.plot(t, z, label="zero" , color="forestgreen")
plt.legend(['d','q','0'])
plt.legend(ncol=3,loc=4)
plt.ylabel("Tensión [Volts]")
plt.xlabel("Tiempo [Segundos]")
plt.title(" Transformación Park (dq0)")
plt.grid('on')
plt.show()


```

## Sistema trifásico balanceado

<img src="https://i.ibb.co/FnrF4KY/Fig01.png" alt="ABC"  />

## Transformación (α, *β*) 

La transformación del marco ABC al sistema de referencia dq0, implementando la misma señal se obtiene con

```python
d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)
```

Un sistema rotatorio puede ser analizado con la transformación de Park generándose dos señales de valor constante  en régimen permanente.

<img src="https://i.ibb.co/BfDjDrj/Fig02.png" alt="Clark" />



## Transformación (ABC) - (dq0)

La transformación del marco ABC al sistema de referencia dq0, implementando la misma señal se obtiene con

```python
d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)
```

Un sistema rotatorio puede ser analizado con la transformación de Park generándose dos señales de valor constante  en régimen permanente.

<img src="https://i.ibb.co/hsJMd1p/Fig03-abc-balance.png" alt="dq0"  />



## Transformación inversa (dq0) - (ABC)

La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes  del dominio del tiempo, marco A, B, C.

```python
a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)
```

## Transformación inversa (α, *β*) - (dq0)

La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes  del dominio del tiempo, marco A, B, C.

```python
d, q, z= ClarkePark.alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)
```


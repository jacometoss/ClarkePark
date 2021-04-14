[![PyPI version](https://badge.fury.io/py/ClarkePark.svg)](https://badge.fury.io/py/ClarkePark)
[![versons of python supported by carsons](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ClarkePark/)
[![Downloads](https://pepy.tech/badge/clarkepark)](https://pepy.tech/project/clarkepark)
[![Downloads](https://pepy.tech/badge/clarkepark/month)](https://pepy.tech/project/clarkepark)
[![Maintainability](https://api.codeclimate.com/v1/badges/6abceb2a140780c13d17/maintainability)](https://codeclimate.com/github/jacometoss/ClarkePark/maintainability)

```text
[Packqge]: ClarkePark 0.1.2
[Autor]: M.Sc.Marco Polo Jácome Toss
[Licencia]: GNU General Public License v3.0
```

# Transformación de Park & Clarke

El módulo de Park (dq0) & Clarke (α, *β* ) incluye :

- Transformación de  componentes del tiempo, marco  A, B, C  a ejes nuevos ejes de referencia estacionario ortogonal   α, *β*.
- Inversa de Clarke, ejes de referencia estacionario ortogonal  α, *β*  a  componentes del dominio del tiempo, marco  A, B , C.
- Transformación de componentes  del tiempo, marco ABC hacia un sistema de referencia dq0 en régimen permanente.
- Inversa de Park, ejes de referencia rotatorio dq0 a componentes  del dominio del tiempo, marco A, B, C.
- Transformación de referencia estacionario ortogonal α, *β* hacia un marco de referencia rotatorio dq0.

## Instalación

La instalación del módulo se realiza con :

```Python
pip install ClarkePark
```

## Transformación (a,b,c) - (α, *β*)

El módulo tiene dependencias siendo necesario instalar `numpy` para procesar la información. También será necesario importar `matplotlib.pyplot` para visualizar los resultados.

```tex
alpha, beta, z = ClarkePark.abc_to_alphaBeta0(A,B,C)
```

Para poder usar la transformación es necesario generar las tres señales monofásicas en desfase y balanceadas.

```python
import ClarkePark
import numpy as np
import matplotlib.pyplot as plt

end_time = 10/float(60)
step_size = end_time/(1000)
t = np.arange(0,end_time,step_size)
wt = 2*np.pi*float(60)*t

rad_angA = float(0)*np.pi/180
rad_angB = float(240)*np.pi/180
rad_angC = float(120)*np.pi/180

A = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
B = (np.sqrt(2)*float(127))*np.sin(wt+rad_angB)
C = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)

alpha, beta, z = ClarkePark.abc_to_alphaBeta0(A,B,C)
```

Graficando se obtiene las señales de tensión (A, B, C)

![ABC](https://i.ibb.co/59wxgbm/02.jpg)



Graficando el marco de referencia (α, *β*)

<img src="https://i.ibb.co/gz1krwx/01.jpg" alt="Clark" />





## Transformación (ABC) - (dq0)

La transformación del marco ABC al sistema de referencia dq0, implementando la misma señal se obtiene con

```python
d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)
```

Un sistema rotatorio puede ser analizado con la transformación de Park generándose dos señales de valor constante  en régimen permanente.

<img src="https://i.ibb.co/MB3Mk68/03.jpg" alt="dq0"  />

## Transformación inversa (dq0) - (ABC)

La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes  del dominio del tiempo, marco A, B, C.

```python
a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)
```

## Transformación marco de referencia (α, *β*) a (dq0)

La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes  del dominio del tiempo, marco A, B, C.

```python
d, q, z= ClarkePark.alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)
```



## Referencias

[1] Kundur, P. (1994). *Power System Stability and Control.* McGraw-Hill Education.

[2]  J.C.DAS. (2016). *Understanding Symmetrical Components for Power System Modeling.* Piscataway: IEEE Press Editorial Board.

[![PyPI version](https://badge.fury.io/py/ClarkePark.svg)](https://badge.fury.io/py/ClarkePark)
[![versons of python supported by carsons](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ClarkePark/)
[![Downloads](https://pepy.tech/badge/clarkepark)](https://pepy.tech/project/clarkepark)
[![Downloads](https://pepy.tech/badge/clarkepark/month)](https://pepy.tech/project/clarkepark)
[![Maintainability](https://api.codeclimate.com/v1/badges/6abceb2a140780c13d17/maintainability)](https://codeclimate.com/github/jacometoss/ClarkePark/maintainability)

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
```

Graficando se obtiene las señales de tensión (A, B, C) balanceada.

<img src="https://i.ibb.co/FnrF4KY/Fig01.png" alt="ABC"  />

Para obtener el gráfico de la tensión trifásica balanceada se uso

```python
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
```

Graficando el marco de referencia (α, *β*)

<img src="https://i.ibb.co/BfDjDrj/Fig02.png" alt="Clark" />

Para obtener el gráfico de la transformación de Clarke

```python
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
```

## Señal trifásica desbalanceada

La señal trifásica desbalanceada únicamente será en la "Fase B" implementaremos las líneas siguientes de código al mostrado al principio.

```
A_unbalance = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
B_unbalance = (np.sqrt(2)*float(115))*np.sin(wt+rad_angB)
C_unbalance = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)
```

Graficando se obtiene las señales de tensión (A, B, C) desbalanceada (Fase B).

![AbC](https://i.ibb.co/gWsM4xw/Fig02abc-Unbalance.png)

Para obtener la señal desbalanceada anterior implemente las siguientes líneas.

```python
plt.figure(figsize=(8,3))
plt.plot(t, A_unbalance, label="A", color='k')
plt.plot(t, B_unbalance, label="B", color='darkred')
plt.plot(t, C_unbalance, label="C", color="darkblue")
plt.legend(['A','B','C'])
plt.legend(ncol=3,loc=4)
plt.ylabel("Tensión [Volts]")
plt.xlabel("Tiempo [Segundos]")
plt.title(" Tensión trifásica (ABC)")
plt.grid('on')
plt.show()
```

Si analizámos la señal con la transformación de Clarke

![TClarke](https://i.ibb.co/XXYSsrn/Fig02-Unbalance.png)

Podemos observar que la componente de secuencia cero tiene oscilaciones debido al desbalance y las componentes alpha y beta no presentan variación alguna. Si implementamos la transformación de Park.

![dq0](https://i.ibb.co/N3mywNs/Fig03-abc-Unbalance.png)

La componente d y  q varían a la misma frecuencia pero la componente de secuencia cero no. A partir de estos ejemplos usted puede implementar el paquete para el manejo y análisis de señales oscilante en el tiempo.



## Transformación (ABC) - (dq0)

La transformación del marco ABC al sistema de referencia dq0, implementando la misma señal se obtiene con

```python
d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)
```

Un sistema rotatorio puede ser analizado con la transformación de Park generándose dos señales de valor constante  en régimen permanente.

<img src="https://i.ibb.co/hsJMd1p/Fig03-abc-balance.png" alt="dq0"  />

Para obtener el gráfico de la transformación de Park

```python
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

## Referencias

[1] Kundur, P. (1994). *Power System Stability and Control.* McGraw-Hill Education.

[2]  J.C.DAS. (2016). *Understanding Symmetrical Components for Power System Modeling.* Piscataway: IEEE Press Editorial Board.

## Autor

```
[Packqge]: ClarkePark 0.1.4
[Autor]: Marco Polo Jácome Toss
[Licencia]: GNU General Public License v3.0
```




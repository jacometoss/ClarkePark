| |image1| |image2| |image3| |image4| |image5|

.. _header-n2:

Instalación de Park & Clarke
============================

La librería Park (dq0) & Clarke (α, *β* ) incluye los módulos siguientes :

-  Transformación de componentes del tiempo, marco A, B, C a ejes nuevos
   ejes de referencia estacionario ortogonal α, *β*.

-  Inversa de Clarke, ejes de referencia estacionario ortogonal α, *β* a
   componentes del dominio del tiempo, marco A, B , C.

-  Transformación de componentes del tiempo, marco ABC hacia un sistema
   de referencia dq0 en régimen permanente.

-  Inversa de Park, ejes de referencia rotatorio dq0 a componentes del
   dominio del tiempo, marco A, B, C.

-  Transformación de referencia estacionario ortogonal α, *β* hacia un
   marco de referencia rotatorio dq0.

.. _header-n15:

Instalación
-----------

La instalación del módulo se realiza con :

.. code:: python

   pip install ClarkePark

.. _header-n18:

Transformación (a,b,c) - (α, *β*)
---------------------------------

El módulo tiene dependencias siendo necesario instalar ``numpy`` para
procesar la información. También será necesario instalar e importar
``matplotlib.pyplot`` para visualizar los resultados.

.. code:: tex

   alpha, beta, z = ClarkePark.abc_to_alphaBeta0(A,B,C)

Las últimas versiones de ``numpy`` y ``matplotlib.pyplot`` pueden ser
utilizadas, el propio paquete las instalará.

.. code:: python

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

Graficando se obtiene las señales de tensión (A, B, C) balanceada.

Para obtener el gráfico de la tensión trifásica balanceada se uso

.. code:: python

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

Graficando el marco de referencia (α, *β*)

Para obtener el gráfico de la transformación de Clarke

.. code:: python

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
   
El arreglo matricial para realizar la transformación que usa el módulo es :

.. math::
   :nowrap:
   
   \begin{eqnarray}

   \begin{matrix}
   \begin{bmatrix}
   i_{\alpha }\left ( t \right )\\ 
   i_{\beta }\left ( t \right )\\
   i_{z\left ( t \right ) }
   \end{bmatrix} =
   \begin{bmatrix}
   1 & -\frac{1}{2} & -\frac{1}{2}\\ 
   0 &  \frac{\sqrt{3}}{2}& -\frac{\sqrt{3}}{2}\\
   \frac{1}{2} & \frac{1}{2} & \frac{1}{2}
   \end{bmatrix}

   \begin{bmatrix}
   i_{a}\left ( t \right )\\ 
   i_{b}\left ( t \right )\\ 
   i_{c}\left ( t \right )
   \end{bmatrix}
   \end{matrix}

   \end{eqnarray}

.. _header-n31:

Señal trifásica desbalanceada
-----------------------------

La señal trifásica desbalanceada únicamente será en la "Fase B"
implementaremos las líneas siguientes de código al mostrado al
principio.

.. code:: python

   A_unbalance = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
   B_unbalance = (np.sqrt(2)*float(115))*np.sin(wt+rad_angB)
   C_unbalance = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)

Graficando se obtiene las señales de tensión (A, B, C) desbalanceada
(Fase B).

.. figure:: https://i.ibb.co/gWsM4xw/Fig02abc-Unbalance.png
   
   Tensión trifásica, sistema ABC

Para obtener la señal desbalanceada anterior implemente las siguientes
líneas.

.. code:: python

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

Si analizámos la señal con la transformación de Clarke

.. figure:: https://i.ibb.co/XXYSsrn/Fig02-Unbalance.png
   
   Transformación de Clarke

Podemos observar que la componente de secuencia cero tiene oscilaciones
debido al desbalance y las componentes alpha y beta no presentan
variación alguna. Si implementamos la transformación de Park.

.. figure:: https://i.ibb.co/N3mywNs/Fig03-abc-Unbalance.png
   
   Transformación de Park

La componente d y q varían a la misma frecuencia pero la componente de
secuencia cero no. A partir de estos ejemplos usted puede implementar el
paquete para el manejo y análisis de señales oscilante en el tiempo.

.. _header-n44:

Transformación (ABC) - (dq0)
----------------------------

La transformación del marco ABC al sistema de referencia dq0,
implementando la misma señal se obtiene con

.. code:: python

   d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)

Un sistema rotatorio puede ser analizado con la transformación de Park
generándose dos señales de valor constante en régimen permanente.

Para obtener el gráfico de la transformación de Park

.. code:: python

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

.. _header-n52:

Transformación inversa (dq0) - (ABC)
------------------------------------

La transformación inversa de Park, ejes de referencia rotatorio dq0 a
componentes del dominio del tiempo, marco A, B, C.

.. code:: python

   a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)

De un marco de referencia constante (dq0) puede ser cambiado al sistema
(ABC) de variables senoidales en el tiempo.

Implementaremos un sistema balanceado y aplicaremos el marco de
referencia constante (dq0) con las líneas siguientes :

.. code:: python

   import ClarkePark
   import numpy as np
   import matplotlib.pyplot as plt

   end_time = 3/float(60)
   step_size = end_time/(1000)
   delta=0
   t = np.arange(0,end_time,step_size)
   wt = 2*np.pi*float(60)*t

   rad_angA = float(0)*np.pi/180
   rad_angB = float(240)*np.pi/180
   rad_angC = float(120)*np.pi/180

   A = (np.sqrt(2)*float(127))*np.sin(wt+rad_angA)
   B = (np.sqrt(2)*float(127))*np.sin(wt+rad_angB)
   C = (np.sqrt(2)*float(127))*np.sin(wt+rad_angC)

   d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)
   a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)

Los resultados obtenidos en líneas anteriores son graficadas mediante

.. code:: python

   plt.figure(figsize=(8,3))
   plt.plot(t, a, label="A", color="royalblue")
   plt.plot(t, b, label="B", color="orangered")
   plt.plot(t, c, label="C" , color="forestgreen")
   plt.legend(['A','B','C'])
   plt.legend(ncol=3,loc=4)
   plt.ylabel("Tensión [Volts]")
   plt.xlabel("Tiempo [Segundos]")
   plt.title(" Sistema trifásico ABC")
   plt.grid('on')
   plt.show()

Finalmente se obtiene las señales del sistema trifásico ABC mediante la
transformación inversa dq0 al sistema ABC.

.. figure:: https://i.ibb.co/gtWbCj7/Figure-2.png
   
   Transformación inversa dq0 - ABC

.. _header-n55:

Transformación inversa (α, *β*) - (dq0)
---------------------------------------

La transformación inversa de Park, ejes de referencia rotatorio dq0 a
componentes del dominio del tiempo, marco A, B, C.

.. code:: python

   d, q, z= ClarkePark.alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)

.. |image1| image:: https://badge.fury.io/py/ClarkePark.svg
   :target: https://badge.fury.io/py/ClarkePark
.. |image2| image:: https://img.shields.io/badge/python-3 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10-blue
   :target: https://pypi.org/project/ClarkePark/
.. |image3| image:: https://pepy.tech/badge/clarkepark
   :target: https://pepy.tech/project/clarkepark
.. |image4| image:: https://pepy.tech/badge/clarkepark/month
   :target: https://pepy.tech/project/clarkepark
.. |image5| image:: https://api.codeclimate.com/v1/badges/6abceb2a140780c13d17/maintainability
   :target: https://codeclimate.com/github/jacometoss/ClarkePark/maintainability

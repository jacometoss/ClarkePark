| |image1|\ |image2|\ |image3|\ |image4|\ |image5|

.. _header-n33:

Marcos de referencia y señal trifásica balanceada
=================================================

Para poder usar la transformación es necesario generar las tres señales
monofásicas en desfase y balanceadas siendo necesario de

-  *Numpy* : Para el manejo de los datos.

-  *Matplotlib* : Obtener las gráficas correspondientes.

.. code-block:: python
   :linenos:
   
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

.. _header-n41:

Sistema trifásico balanceado
----------------------------

.. _header-n43:

Transformación (*α*, *β*) 
-----------------------

La transformación del marco ABC al sistema de referencia α, *β*,
implementando la misma señal se obtiene con

.. code:: python

  alpha, beta, z = ClarkePark.abc_to_alphaBeta0(A,B,C)

Un sistema rotatorio puede ser analizado con la transformación de Park
generándose dos señales de valor constante en régimen permanente.

.. _header-n49:

Transformación (ABC) - (dq0)
----------------------------

La transformación del marco ABC al sistema de referencia dq0,
implementando la misma señal se obtiene con

.. code:: python

   d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)

Un sistema rotatorio puede ser analizado con la transformación de Park
generándose dos señales de valor constante en régimen permanente.

.. _header-n55:

Transformación inversa (dq0) - (ABC)
------------------------------------

La transformación inversa de Park, ejes de referencia rotatorio dq0 a
componentes del dominio del tiempo, marco A, B, C.

.. code:: python

   a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)

.. _header-n58:

Transformación inversa (*α*, *β*) - (dq0)
---------------------------------------

La transformación inversa de Park, ejes de referencia rotatorio dq0 a
componentes del dominio del tiempo, marco A, B, C.

.. code:: python

   d, q, z= ClarkePark.alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)

.. |image1| image:: https://badge.fury.io/py/ClarkePark.svg
   :target: https://badge.fury.io/py/ClarkePark
.. |image2| image:: https://img.shields.io/badge/python-3 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9-blue
   :target: https://pypi.org/project/ClarkePark/
.. |image3| image:: https://pepy.tech/badge/clarkepark
   :target: https://pepy.tech/project/clarkepark
.. |image4| image:: https://pepy.tech/badge/clarkepark/month
   :target: https://pepy.tech/project/clarkepark
.. |image5| image:: https://api.codeclimate.com/v1/badges/6abceb2a140780c13d17/maintainability
   :target: https://codeclimate.com/github/jacometoss/ClarkePark/maintainability

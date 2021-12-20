Módulos ClarkePark
==================

Descripción
-----------

:program:`ClarkePark` presenta los módulos siguientes:

.. option:: Transformación (abc) -> (alpha,beta)

   La transformación del marco ABC al sistema de referencia α, β, implementando la misma señal se obtiene con

.. code:: python

   alpha, beta, z = ClarkePark.abc_to_alphaBeta0(ABC)
   

.. option:: Transformación (ABC) -> (dq0)

   La transformación del marco ABC al sistema de referencia dq0, implementando la misma señal se obtiene con
   
.. code:: python

   d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)

.. option:: Transformación inversa (dq0) - (ABC)

   La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes del dominio del tiempo, marco A, B, C.
   
.. code:: python

   a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)

.. option:: Transformación inversa (alpha,beta) - (dq0)

   La transformación inversa de Park, ejes de referencia rotatorio dq0 a componentes del dominio del tiempo, marco A, B, C.
   
.. code:: python

   d, q, z= ClarkePark.alphaBeta0_to_dq0(alpha, beta, zero, wt, delta)

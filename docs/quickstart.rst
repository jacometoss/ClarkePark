ClarkePark
===========

.. option:: Transformación (abc) -> (αβ)

.. code:: python

   alpha, beta, z = ClarkePark.abc_to_alphaBeta0(ABC)
   

.. option:: Transformación (ABC) -> (dq0)

.. code:: python

   d, q, z = ClarkePark.abc_to_dq0(A, B, C, wt, delta)

.. option:: Transformación inversa (dq0) - (ABC)

.. code:: python

   a, b, c = ClarkePark.dq0_to_abc(d, q, z, wt, delta)


Simulación de la Maquina de Inducción 2250 Hp
=============================================

En este ejemplo simulares las corrientes del estator de la máquina de
inducción de 2250 Hp. Para leer los resultados guardados se ocupa
`Pandas <https://pandas.pydata.org/>`__ de esta manera las columnas del
fichero fueron nombradas, los resultados del fichero se obtienen
mediante el bloque de código siguiente :

.. code:: python

   import pandas as pd
   db = pd.read_csv('simulacionMI2250HP.csv')
   t=db.t
   ias=db.ias
   ibs=db.ibs
   ics=db.ics

La corriente en estator cuando arranca la Maquina de Inducción de 2250
Hp es :

|image1|

Fig. 1.- Corrientes en el estator.

El bloque de código para graficar la señal es :

.. code:: python

   plt.figure(figsize=(8,3))
   plt.plot(t, ias, label="ias", color='k')
   plt.plot(t, ibs, label="ibs", color='darkred')
   plt.plot(t, ics, label="ics", color="darkblue")
   plt.legend(['ias','ibs','ics'])
   plt.legend(ncol=3,loc=4)
   plt.ylabel("Corriente [Amperios]")
   plt.xlabel("Tiempo [Segundos]")
   plt.title(" Motor de Inducción 2550Hp Corrientes Estátor")
   plt.grid('on')
   plt.show()

.. _transformación-abc-al-sistema-de-referencia-α-β:

Transformación ABC al sistema de referencia α, *β*.
===================================================

La transformación del marco ABC al sistema de referencia α, *β* se
obtiene mediante el código siguiente :

.. code:: python

   alpha, beta, z = ClarkePark.abc_to_alphaBeta0(ias,ibs,ics)

   plt.figure(figsize=(8,3))
   plt.plot(t, alpha, label="\u03B1", color="darkred")
   plt.plot(t, beta, label="\u03B2", color="darkblue")
   plt.plot(t, z, label="zero" , color="dimgray")
   plt.legend(['\u03B1','\u03B2','0'])
   plt.legend(ncol=3,loc=4)
   plt.ylabel("Corriente Estátor [Amperios]")
   plt.xlabel("Tiempo [Segundos]")
   plt.title(" Transformación Clarke Motor Inducción 2250Hp (\u03B1 \u03B2)")
   plt.grid('on')
   plt.show()

De esta manera se obtiene la gráfica

.. figure:: https://i.ibb.co/9cLwWP1/Corriente-estator-alpha-beta.png
   :alt: 

Fig. 2.- Corrientes en el estator.

Realizando un acercamiento a la figura 2.

.. figure:: https://i.ibb.co/f40qFSs/Corriente-estator-alpha-beta-zoom.png
   :alt: 

.. |image1| image:: https://i.ibb.co/vsdkCyC/Corriente-estator-abc.png

Fig. 3.- Acercamiento Fig. 2 .

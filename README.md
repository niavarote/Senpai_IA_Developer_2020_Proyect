# Senpai_IA_Developer_2020_Proyect
Proyecto de IA para la aprobacion del curso IA Developer - Consumo de combustible de Vehiculos.

INDICE
1- Conformación del equipo ya definida.
2- Descripción de la problemática a solucionar.
3- Descripción de la solución inicial planteada.
4- Descripción inicial del algoritmo de machine learning o modelo de deep learning a
utilizar.
5- Análisis de soluciones existentes y detalle de la alternativa seleccionada


# 1 - Conformación del equipo ya definida.
Por temas de tiempos laborales, la decision fue hacerlo individual.

# 2 - Descripción de la problemática a solucionar.
Luego de buscar diferentes casos para trabajar en el proyecto me decidi por plantear al docente una problematica personal actual, esta consta en poder inferir/predecir el consumo de un vehiculo dados ciertos datos basicos, como puede ser, cilindrada, transmicion, etc,.. Este problematica  personal surguio al buscar un automovil de consumo  economico en sitios de ventas online (mercadolibre),como regla casi general, los vendedores no proveer ese dato tan importante el cual puede partir no por error del vendedor sino que a veces sucede que el fabricante no lo proporciona por estrategias de marketing. Por la cantidad de esos casos que surgen en el  mercado se me ocurrio este proyecto , planteado luego al docente y confirmado para su investigacion y ejecucion.
Antes de plantear la problematica se investigo si se tenian los datos adecuados para atacarla y/o si se podia extraer de algunas fuentes, teniando los datos minimos necesarios para su tratamiento a este problema de "regresion escalar"

# 3 - Descripción de la solución inicial planteada.

La propuesta es poder predecir el consumo de combustible de un automovil que actualmente este circulando en el mercado regional, para poder lograrlo se proveera al modelo la descripcion de los automoviles como ser tipoVehiculo,traccion,cilindrada,etc.

Para este proyecto vamos a extraer un set de datos de la web consumovehicular.cl(actualmente 2850 vehiculos a gasolina), asi como agregaremos los vehiculos mas comunes del mercado uruguayo, extrayendo manualmente de las webs correspondientes (fiat,renault,etc).

Descripcion de algunos campos/informacion de entrada:

rendimientoMixto(consumo) -> variable continua (a predecir)

cilindrada->  variable dicreta de valores multiples

traccion->variable categorica

transmision->variable categorica

norma-> variable categorica

....

Con la entrada de datos obtenida ya podemos tomar como validos para poder inferir sobre estos, la salida del modelo requerida (consumo).

Como scaprinig inicial de los datos en este pre-proyecto definimos el archivo 1-Scraping_Data.ipynb definida en la en esta pre-entrega

Para esta hipotisis poderemos inferir el consumo pero soy conciente que de que podria darse casos que la muestra de entrada no sea suficiente informacion para hacer una prediccion efectiva. 

Este caso se trata de un aprendizaje supervisado, dado que tenemos etiquetado el campo rendimientoMixto y se lo proporcionamos al modelo para su entrenamiento. Tambien lo podemos catalogar como un problema de regresion, especificamente de regresion multiple , esto se da porque se dan "multiples" variables de entrada para realizar la prediccion.

Luego de tener los datos del scraping y de la insercion manual, vamos a preparar los datos sobre el archivo 2-Data_transformation.ipynb, en el vamos a eliminar campos inutiles, categorizar algunas columnas, eliminar filas con datos faltantes,etc

Continuaremos separando el dataset en conjuntos de entrenamiento, validacion y prueba
Normalizamos los datos

# 4- Descripción inicial del algoritmo de machine learning o modelo de deep learning a utilizar.

Para la red neuronal a usar definimos primero la ultima capa a utilizar , esta es una capa densa(1) por esperar solo un valor continuo de salida.
Luego como arquitecturas de las capas inciales estas seran 2 capas densas de 64 neuronas inicialmente, claro esta que este modelo puede tener alteraciones, mientras se avanza en la investigacion y pruebas del caso. El archivo notebook a trabajar sera llamado 3_Training_and_evaluate.ipynb.

Como funcion de perdida probare con las tradicionales para tareas de regresion, MSE(mean square error) y MAE(Mean absolute error)

Inicialmente como  Optimizador utilizare RMSprop y correremos unos 1000 epocks para luego ver y analizar si existe overfitting/underfitting(como pruebas) en caso que exista utilizaremos la funcion earlystopping de keras para que se quede con la mejor muestra.

Luego de ajustar los hiperparametros los mas posibles obtenderemos y modelo final el cual lo pasaremos como archivo a una solucion alojada en python flask para ser llamada por Rest (endpoint) desde una app web plublicada...

El archivo del modelo se guardara con nombre cars_model.h5, este sera el usado en la app web en flask para inferir el consumo de un vehiculo.


# 5- Análisis de soluciones existentes y detalle de la alternativa seleccionada

Realmente para este caso, me base en investigar los casos de regresion lineal de varios temas , no encontrando inicialmente ningun ejemplo claro, al dia de hoy 07/06/2020 se encontro un ejemplo de tensorflow con el mismo objetivo, se estudio el ejemplo y se sacaron ideas para la implementacion de este proyecto.

Algunas web de investigacion tomadas en cuenta:
https://machinelearningmastery.com/how-to-make-classification-and-regression-predictions-for-deep-learning-models-in-keras/

Ejemplo de regresion para calculo de MPG de un vehiculo.
https://www.tensorflow.org/tutorials/keras/regression?hl=es


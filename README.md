# Senpai_IA_Developer_2020_Proyect
Proyecto de IA para la aprobacion del curso IA Developer - Consumo de combustible de Vehiculos.

INDICE
Pre-Proyecto
1- Conformación del equipo ya definida.
2- Descripción de la problemática a solucionar.
3- Descripción de la solución inicial planteada.
4- Descripción inicial del algoritmo de machine learning o modelo de deep learning a
utilizar, descripcion detallada.
5- Análisis de soluciones existentes y detalle de la alternativa seleccionada

Proyecto Final
6- Detalle de la arquitectura, que cambio.
7- Paso a Paso de como correr la solucion.



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

# 6- Proyecto final, Detalle de la arquitectura, que cambio..
Para el proyecto final se agregaron algunos cambios observados en la correcion del preproyecto descripto hasta el punto 5 inclusive de este documento,asi como nuevos aprendimientos aplicados sobre la marcha. Los detalles de los pormenores del proyecto, se explican sobre las notebooks correspondientes.
Estos fueron:
-Se agrego la funcion de callback EarlyStopping, esta, interrumpe el entrenamiento cuando las metricas de la funcion de perdida, para los datos de validacion, no mejoran luego de 20 epocks, aplicados sobre la notebook 3-Training_and_evaluate.ipynb
-Se eliminaron columnas no importantes o que podrian alterar la prediccion final de los datos, contanto tambien que serian muy dificiles de adquirir por el usuario final.
Estos fueron 'co2','rendimientoCarretera','rendimientoUrbano' aplicados en la notebook 2-Data_Transformation.ipynb.
-Se probaron modificar algunos hiperparametros para ver si se podia optimizar aun mas el resultado final. 3-Training_and_evaluate.ipynb
-Se agrego un servicio HTTP hecho sobre el server Flask para exponer una API para el consumo del cliente final, el archivo endpoint.py explica como correr el server y ejecutar un request desde CURL.

# 7- Paso a Paso de como correr la solucion.
Situado en el mismo directorio del proyecto ,ejecutar el comando desde la consola: "python endpoint.py" este ejecuta el servidor flask dejando disponible el servicio de prediccion. Retorna la siguiente salida:
   Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Probar el script ejecutando el siguiente curl:
curl --location --request POST 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
"cilindrada":{"0":1.4},
"EURO V":{"0":1.0},
"EURO VI":{"0":0.0},
"TIER 3 B50":{"0":0.0},
"TIER 2 B5":{"0":0.0},
"EURO V":{"0":0.0},
"EURO VI":{"0":0.0},
"TIER 3 B50":{"0":0.0},
"TIER 2 B5":{"0":0.0},
"TIER 2 B4":{"0":0.0},
"TIER 3 B70":{"0":0.0},
"TIER 2 B6":{"0":0.0},
"TIER 2 B8":{"0":0.0},
"Tier 3 B125":{"0":0.0},
"TIER 3 B125":{"0":0.0},
"TIER 3 B30":{"0":0.0},
"Hatch Back":{"0":1.0},
"Sed\u00e1n":{"0":0.0},
"Station Wagon":{"0":0.0},
"Cabriolet":{"0":0.0},
"Coup\u00e9":{"0":0.0},
"Convertible":{"0":0.0},
"Furg\u00f3n":{"0":0.0},
"Jeep":{"0":0.0},
"Limusina":{"0":0.0},
"Roadster":{"0":0.0},
"Camioneta":{"0":0.0},
"Minivan":{"0":0.0},
"Furg\u00f3n Cerrado":{"0":0.0},
"Minibus":{"0":0.0},
"Microvan":{"0":0.0},
"4x2":{"0":1.0},
"4x4":{"0":0.0},
"M":{"0":1.0},
"A":{"0":0.0}
}'
        
Los datos unicos a ingresar seran: 
1- Cilindrada, con el formato X.X ejemplo 1.0, 1.4, 2.0 
2- Norma(Tipo de motor), marcar con 1.0(activo) en caso contrario 0.0, es el tipo de motor cuenta el auto que va desde "EURO V" a  "TIER 3 B30" solo una opcion es activada.
3- Tipo de Vehiculo que va desde "Hatch Back" a "Microvan", solo uno se activa con "1.0"
4- Traccion "4x2" o "4x4", solo uno se activa con "1.0" 
5- Transmision(Tipo de caja de cambio M(manual) o A(automatica))

Cabe mencionar que al final del archivo 3_Training_and_evaluate.ipynb. se pueden realizar predicciones de pruebas sobre el dataset de datos de pruebas disponibles.
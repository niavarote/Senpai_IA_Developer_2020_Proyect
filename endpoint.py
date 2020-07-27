'''
Ejecutar el comando desde la consola: "python endpoint.py". Se debería ver la salida:
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
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
        
'''
# Imports necesarios
from __future__ import print_function
import tensorflow as tf
import keras
import numpy as np
import flask
import io
import json
import pandas as pd
from keras.models import load_model

#from flask import Flask, request, render_template, jsonify
#from flask_request_params import bind_request_params

# Inicializar aplicación Flask
app = flask.Flask(__name__)
model = None
train_stats = None

def load_trained_model():
    print("Cargando modelo de Keras...")

    global model
    global train_stats
    global train_stats_mixto

    model = tf.keras.models.load_model('cars_model.h5')
    model._make_predict_function()
    #cargo los datos utilizados para normalizar y escalar usado en los datos de entrenamiento
    train_stats=pd.read_json("3_train_stats.json", orient="columns")
    print("Modelo cargado")

'''
Nuestra  función que contesta un JSON como el siguiente:
{
    "predicted": "[11.060342]",
    "success": true
}
'''

#funcion para normalizar y escalar los datos de entrada
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']

def denorm(X_s):
  return X_s * train_stats_mixto['std']['rendimientoMixto'] + train_stats_mixto['mean']['rendimientoMixto']

#funcion principal predict
@app.route("/predict", methods=["POST"])
def predict():
    # Inicializo retorno
    data = {"success": False}

    if flask.request.method == "POST":
            content = flask.request.json
            df=pd.DataFrame(eval(content.__str__()))
            normed_data = norm(df)
            Xnew = model.predict(normed_data)
            data["predicted"]=Xnew[0].__str__()
            data["success"] = True
            print("Predicted=%s" % (Xnew[0]))
    # Contesto un JSON
    return flask.jsonify(data)

# Comenzar la ejecución del servidor
if __name__ == "__main__":
    print("Inicializando servidor")
    load_trained_model()
    app.run(debug=False)
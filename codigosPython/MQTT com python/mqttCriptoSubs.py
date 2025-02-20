# Subscriber criptografado 

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Criptografia import cifraSimples # Biblioteca de criptografia

import paho.mqtt.client as paho
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"CONNACK recebido com o código: {rc}")

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"Inscrito: {str(mid)}, {str(granted_qos)} ")

def on_message(client, userdata, msg):
    print(f"Tópico: {msg.topic}\nMenssagem : {cifraSimples.cripto(msg.payload.decode())}\n")

# ------------- Conexão padrão -------------
cliente = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
cliente.on_connect = on_connect

cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.username_pw_set("Subscriber", "12341234") 
cliente.connect("f5676352a6d24d37b55cdd9d249f3c6f.s1.eu.hivemq.cloud", 8883)


# ------------- Subscriber -------------
print("Terminal do subscriber")
cliente.subscribe("msgCriptografada", qos=1)
cliente.on_subscribe = on_subscribe # Mostra o Tópico inscrito e o QoS
cliente.on_message = on_message


cliente.loop_forever()
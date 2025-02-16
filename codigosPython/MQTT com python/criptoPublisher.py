# Esse arquivo atuara como publisher das informações recebidas via serial do esp32 ou arduino, codiicara e as enviará para o broker


# --------------------- Adiciona o diretório raiz ao sys.path ---------------------
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Criptografia import cifraSimples # Biblioteca de criptografia

# ----------------------------------------------------------------------------------

import paho.mqtt.client as paho 
from paho import mqtt
from time import sleep

def on_connect(client, userdata, rc, properties=None):
    print(f"CONNACK --> {rc}")

def on_publishe(client, userdata, mid, properties=None):
    print(f"mid: {str(mid)}")

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5) # Configuração do cliente e versão do MQTT
client.on_connect = on_connect # Callback da criação do cliente

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set("Publisher", "27724991Jp!")
client.connect("f5676352a6d24d37b55cdd9d249f3c6f.s1.eu.hivemq.cloud", 8883)


client.loop_forever()
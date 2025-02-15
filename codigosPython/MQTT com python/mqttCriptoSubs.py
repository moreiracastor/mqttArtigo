# Subscriber criptografado 

import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
from paho import mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"CONNACK recebido com o código: {rc}")

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"Inscrito: {str(mid)}, {str(granted_qos)} ")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")

# ------------- Conexão padrão -------------
cliente = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
cliente.on_connect = on_connect

cliente.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

cliente.username_pw_set("Subscriber", "27724991Jp!") 
cliente.connect("f5676352a6d24d37b55cdd9d249f3c6f.s1.eu.hivemq.cloud", 8883)
cliente.on_message = on_message


# ------------- Subscriber -------------
print("Terminal do subscriber")
cliente.subscribe("ola", qos=0)
cliente.on_subscribe = on_subscribe # Mostra o Tópico inscrito e o QoS


cliente.loop_forever()
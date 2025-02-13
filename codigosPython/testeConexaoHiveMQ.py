import time
import paho.mqtt.client as paho
from paho import mqtt

# Configuração dos Callbacks para diferentes eventos, se funcionar exibe uma menssagem
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# Com esse Callback você consegue ver se a sua publilcação foi bem sucedida
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# Mostar qual tópico que você se inscreveu
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# Imprime a menssagem, o tópico e o payload, usado para verificar se foi enviada
# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client

# Característica do MQTT 5
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5) 
client.on_connect = on_connect

# Ativa o TLS para a segurança
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# Configura i Username e a Senha
client.username_pw_set("JotaPe", "27724991Jp!")
# Conecta a URL do Cluster e a porta padrão 8883
client.connect("f5676352a6d24d37b55cdd9d249f3c6f.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

#Para se inscrever em todos os tópicos filhos de um tópico mãe se usa #
# subscribe to all topics of encyclopedia by using the wildcard "#"

# Se inscreve no tópico "ola"
client.subscribe("ola", qos=1)

# Uma públicação unica no tópico "ola" com a menssagem e com o QoS .publish("tópico", payload="Menssagem", qos="Método de segurança")
client.publish("ola", payload="Ola Mundo, agora do Python", qos=1)


client.loop_forever() # Esse loop serve para facilitar a reprodução do código
                      # Poderia ser substiuido por loop_start e o loop_stop

# Mudança do tópico principal e da mensagem, tradução dos comentários presentes no código
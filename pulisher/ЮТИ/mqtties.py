import paho.mqtt.client as mqtt
import time
from PIL import Image
import io
from numpy import asarray

BROKER_ADDRESS = "broker.hivemq.com"  # Адрес брокера
PORT = 1883  # Порт по умолчанию для MQTT
TOPIC_SUBSCRIBE = "img/receive"  # Топик для подписки
TOPIC_PUBLISH = "img/receive"  # Топик для публикации


def image_to_byte_array():
    with open('webka.jpg', 'rb') as img:
        b = bytearray(img.read())
        return b


# Callback при подключении к брокеру
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.subscribe(TOPIC_SUBSCRIBE)  # Подписка на топик при успешном подключении
    else:
        print(f"Connection error: {rc}")


# Callback при получении сообщения
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} from topic {msg.topic}")


# Callback при публикации сообщения
def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")


def publishing():
    # Инициализация клиента
    client = mqtt.Client()
    client.on_connect = on_connect

    # Подключение к брокеру
    client.connect(BROKER_ADDRESS, PORT, 60)

    # Запуск цикла обработки сообщений в фоновом потоке
    client.loop_start()

    # Публикация сообщения
    try:
        while True:
            a = image_to_byte_array()
            client.publish(TOPIC_PUBLISH, a)
            print(f"Sent: {a}")
            time.sleep(10)

    except KeyboardInterrupt:
        print("Disconnecting...")
        client.loop_stop()
        client.disconnect()

import paho.mqtt.client as mqtt
import time
import cv2
import numpy as np

# Параметры подключения
BROKER_ADDRESS = "broker.hivemq.com"  # Адрес брокера
PORT = 1883  # Порт по умолчанию для MQTT
TOPIC_SUBSCRIBE = "test/topic"  # Топик для подписки
TOPIC_PUBLISH = "test/topic"  # Топик для публикации


# Callback при подключении к брокеру
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.subscribe(TOPIC_SUBSCRIBE)  # Подписка на топик при успешном подключении
    else:
        print(f"Connection error: {rc}")


# Callback при получении сообщения
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload}")
    np_array = np.asarray(msg.payloadL, dtype=np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    cv2.imwrite('output.jpg', image)


# Callback при публикации сообщения
def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")


# Инициализация клиента
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

# Подключение к брокеру
client.connect(BROKER_ADDRESS, PORT, 60)

# Запуск цикла обработки сообщений в фоновом потоке
client.loop_start()

# Публикация сообщения
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")
    client.loop_stop()
    client.disconnect()
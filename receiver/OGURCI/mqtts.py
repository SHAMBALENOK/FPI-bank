import paho.mqtt.client as mqtt
import time
import PIL.Image as Image
import cv2
from io import BytesIO
import main


# Параметры подключения
BROKER_ADDRESS = "broker.hivemq.com"  # Адрес брокера
PORT = 1883  # Порт по умолчанию для MQTT
TOPIC_SUBSCRIBE = "img/receive"  # Топик для подписки
TOPIC_PUBLISH = "img/receive"  # Топик для публикации


# Callback при подключении к брокеру
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.subscribe(TOPIC_SUBSCRIBE)  # Подписка на топик при успешном подключении
    else:
        print(f"Connection error: {rc}")


# Callback при получении сообщения
def on_message(client, userdata, msg):
    message = msg.payload
    print(f"Received message: {message}")
    img_bytes = bytearray(message)
    new_img = Image.open(BytesIO(img_bytes))
    new_img.save('new_img.png')
    main.f()



# Callback при публикации сообщения
def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")


# Инициализация клиента
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

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
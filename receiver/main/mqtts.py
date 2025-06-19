import PIL
import paho.mqtt.client as mqtt
import time
import PIL.Image as Image
import cv2
from io import BytesIO
import recognition

# Параметры подключения
BROKER_ADDRESS = "broker.hivemq.com"  # Адрес брокера
PORT = 1883  # Порт по умолчанию для MQTT
TOPIC_SUBSCRIBE = "img/receive"  # Топик для подписки
TOPIC_PUBLISH = "img/receive"  # Топик для публикации


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.subscribe(TOPIC_SUBSCRIBE)  # Подписка на топик при успешном подключении
    else:
        print(f"Connection error: {rc}")


# Callback при получении сообщения
def on_message(client, userdata, msg):
    global client_mqtt
    message = msg.payload
    img_bytes = bytearray(message)
    try:
        new_img = Image.open(BytesIO(img_bytes))
        new_img.save('new_img.png')
        try:
            print('\nПолученно изображение', end=' ')
            res = recognition.f()
            time.sleep(1)
            if res[0]:
                client_mqtt.publish(TOPIC_PUBLISH, f'это {res[1]}')
            else:
                client_mqtt.publish(TOPIC_PUBLISH, f'это неизвестный')
        except IndexError:
            pass
    except PIL.UnidentifiedImageError:
        pass


# Callback при публикации сообщения
def on_publish(client, userdata, mid):
    print(f"Message published (mid: {mid})")


client_mqtt = mqtt.Client()
client_mqtt.on_connect = on_connect
client_mqtt.on_message = on_message

# Подключение к брокеру
client_mqtt.connect(BROKER_ADDRESS, PORT, 60)
# Запуск цикла обработки сообщений в фоновом потоке
client_mqtt.loop_start()

# Публикация сообщения
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")
    client_mqtt.loop_stop()
    client_mqtt.disconnect()

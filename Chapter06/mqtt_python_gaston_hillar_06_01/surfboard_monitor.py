"""
Book: Hands-On MQTT Programming with Python
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from config import *
from surfboard_status import *
from surfboard_config import *
import paho.mqtt.client as mqtt
import time
import json


# Publish key is the one that usually starts with the "pub-c-" prefix
# Do not forget to replace the string with your publish key
pubnub_publish_key = "pub-c-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# Subscribe key is the one that usually starts with the "sub-c" prefix
# Do not forget to replace the string with your subscribe key
pubnub_subscribe_key = "sub-c-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
pubnub_mqtt_server_host = "mqtt.pndsn.com"
pubnub_mqtt_server_port = 1883
pubnub_mqtt_keepalive = 60
device_id = surfboard_name
pubnub_topic = surfboard_name


class Surfboard:
    active_instance = None
    def __init__(self, device_id, status, 
        speed_mph, altitude_feet, water_temperature_f):
        self.device_id = device_id
        self.status = status
        self.speed_mph = speed_mph
        self.altitude_feet = altitude_feet
        self.water_temperature_f = water_temperature_f
        self.is_pubnub_connected = False
        Surfboard.active_instance = self

    def build_json_message(self):
        # Build a message with the status for the surfboard
        message = {
            "Status": SURFBOARD_STATUS_DICTIONARY[self.status],
            "Speed MPH": self.speed_mph,
            "Altitude Feet": self.altitude_feet,
            "Water Temperature F": self.water_temperature_f, 
        }
        json_message = json.dumps(message)
        return json_message


def on_connect_mosquitto(client, userdata, flags, rc):
    print("Result from Mosquitto connect: {}".format(
        mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED connack code
    if rc == mqtt.CONNACK_ACCEPTED:
        # Subscribe to a topic filter that provides all the sensors
        sensors_topic_filter = topic_format.format(
            surfboard_name,
            "+")
        client.subscribe(sensors_topic_filter, qos=0)


def on_subscribe_mosquitto(client, userdata, mid, granted_qos):
    print("I've subscribed with QoS: {}".format(
        granted_qos[0]))


def print_received_message_mosquitto(msg):
    print("Message received. Topic: {}. Payload: {}".format(
        msg.topic, 
        str(msg.payload)))


def on_status_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Surfboard.active_instance.status = int(msg.payload)


def on_speed_mph_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Surfboard.active_instance.speed_mph = float(msg.payload)


def on_altitude_feet_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Surfboard.active_instance.altitude_feet = float(msg.payload)


def on_water_temperature_f_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Surfboard.active_instance.water_temperature_f = float(msg.payload)


def on_connect_pubnub(client, userdata, flags, rc):
    print("Result from PubNub connect: {}".format(
        mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED connack code
    if rc == mqtt.CONNACK_ACCEPTED:
        Surfboard.active_instance.is_pubnub_connected = True


def on_disconnect_pubnub(client, userdata, rc):
    Surfboard.active_instance.is_pubnub_connected = False
    print("Disconnected from PubNub")


if __name__ == "__main__":
    surfboard = Surfboard(device_id=device_id,
        status=SURFBOARD_STATUS_IDLE,
        speed_mph=0, 
        altitude_feet=0, 
        water_temperature_f=0)
    pubnub_client_id = "{}/{}/{}".format(
        pubnub_publish_key,
        pubnub_subscribe_key,
        device_id)
    pubnub_client = mqtt.Client(client_id=pubnub_client_id,
        protocol=mqtt.MQTTv311)
    pubnub_client.on_connect = on_connect_pubnub
    pubnub_client.on_disconnect = on_disconnect_pubnub
    pubnub_client.connect(host=pubnub_mqtt_server_host,
        port=pubnub_mqtt_server_port,
        keepalive=pubnub_mqtt_keepalive)
    pubnub_client.loop_start()
    mosquitto_client = mqtt.Client(protocol=mqtt.MQTTv311)
    mosquitto_client.on_connect = on_connect_mosquitto
    mosquitto_client.on_subscribe = on_subscribe_mosquitto
    mosquitto_client.message_callback_add(
        status_topic,
        on_status_message_mosquitto)
    mosquitto_client.message_callback_add(
        speed_mph_topic,
        on_speed_mph_message_mosquitto)
    mosquitto_client.message_callback_add(
        altitude_feet_topic,
        on_altitude_feet_message_mosquitto)
    mosquitto_client.message_callback_add(
        water_temperature_f_topic,
        on_water_temperature_f_message_mosquitto)
    mosquitto_client.tls_set(ca_certs = ca_certificate,
        certfile=client_certificate,
        keyfile=client_key)
    mosquitto_client.connect(host=mqtt_server_host,
        port=mqtt_server_port,
        keepalive=mqtt_keepalive)
    mosquitto_client.loop_start()
    try:
        while True:
            if Surfboard.active_instance.is_pubnub_connected:
                payload = Surfboard.active_instance.build_json_message()
                result = pubnub_client.publish(topic=pubnub_topic,
                    payload=payload,
                    qos=0)
                print("Publishing: {}".format(payload))
            else:
                print("Not connected")
            time.sleep(1)
    except KeyboardInterrupt:
        print("I'll disconnect from both Mosquitto and PubNub")
        pubnub_client.disconnect()
        pubnub_client.loop_stop()
        mosquitto_client.disconnect()
        mosquitto_client.loop_stop()

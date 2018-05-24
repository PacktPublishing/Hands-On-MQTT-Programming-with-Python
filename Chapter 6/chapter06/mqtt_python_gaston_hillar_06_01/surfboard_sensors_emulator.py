"""
Book: Hands-On MQTT Programming with Python
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from config import *
from surfboard_config import *
import paho.mqtt.client as mqtt
import time
import csv


def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(
        mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED connack code
    if rc != mqtt.CONNACK_ACCEPTED:
        raise IOError("I couldn't establish a connection with the MQTT server")

def publish_value(client, topic, value):
    result = client.publish(topic=topic,
        payload=value,
        qos=0)
    return result


if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.tls_set(ca_certs = ca_certificate,
        certfile=client_certificate,
        keyfile=client_key)
    client.connect(host=mqtt_server_host,
        port=mqtt_server_port,
        keepalive=mqtt_keepalive)
    client.loop_start()
    publish_debug_message = "{}: {}"
    try:
        while True:
            with open('surfboard_sensors_data.csv') as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    status_value = int(row[0])
                    speed_mph_value = float(row[1])
                    altitude_feet_value = float(row[2])
                    water_temperature_f_value = float(row[3])
                    print(publish_debug_message.format(
                        status_topic,
                        status_value))
                    print(publish_debug_message.format(
                        speed_mph_topic, 
                        speed_mph_value))
                    print(publish_debug_message.format(
                        altitude_feet_topic, 
                        altitude_feet_value))
                    print(publish_debug_message.format(
                        water_temperature_f_topic, 
                        water_temperature_f_value))
                    publish_value(client, 
                        status_topic, 
                        status_value)
                    publish_value(client, 
                        speed_mph_topic, 
                        speed_mph_value)
                    publish_value(client, 
                        altitude_feet_topic, 
                        altitude_feet_value)
                    publish_value(client,
                        water_temperature_f_topic, 
                        water_temperature_f_value)
                    time.sleep(1)
    except KeyboardInterrupt:
        print("I'll disconnect from the MQTT server")
        client.disconnect()
        client.loop_stop()

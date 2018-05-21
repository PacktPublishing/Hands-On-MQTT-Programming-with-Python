"""
Book: Hands-On MQTT Programming with Python
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
import os.path


# Replace /Users/gaston/python_certificates with the path
# in which you saved the certificate authority file,
# the client certificate file and the client key
certificates_path = "/Users/gaston/python_certificates"
ca_certificate = os.path.join(certificates_path, "ca.crt")
client_certificate = os.path.join(certificates_path, "board001.crt")
client_key = os.path.join(certificates_path, "board001.key")
# Replace 192.168.1.104 with the IP or hostname for the Mosquitto
# or other MQTT server
# Make sure the IP or hostname matches the value 
# you used for Common Name
mqtt_server_host = "192.168.1.104"
mqtt_server_port = 8883
mqtt_keepalive = 60

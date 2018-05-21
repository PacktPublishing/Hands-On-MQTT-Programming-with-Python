"""
Book: Hands-On MQTT Programming with Python
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
surfboard_name = "surfboard01"
topic_format = "surfboards/{}/{}"
status_topic = topic_format.format(
    surfboard_name, 
    "status")
speed_mph_topic = topic_format.format(
    surfboard_name, 
    "speedmph")
altitude_feet_topic = topic_format.format(
    surfboard_name, 
    "altitudefeet")
water_temperature_f_topic = topic_format.format(
    surfboard_name, 
    "temperaturef")

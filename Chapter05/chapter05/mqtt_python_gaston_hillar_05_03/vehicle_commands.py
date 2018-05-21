"""
Book: Hands-On MQTT Programming with Python
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
# Key strings
COMMAND_KEY = "CMD"
SUCCESFULLY_PROCESSED_COMMAND_KEY = "SUCCESSFULLY_PROCESSED_COMMAND"
# Command strings
# Turn on the vehicle’s engine
CMD_TURN_ON_ENGINE = "TURN_ON_ENGINE"
# Turn off the vehicle’s engine
CMD_TURN_OFF_ENGINE = "TURN_OFF_ENGINE"
# Close and lock the vehicle’s doors
CMD_LOCK_DOORS = "LOCK_DOORS"
# Unlock and open the vehicle’s doors
CMD_UNLOCK_DOORS = "UNLOCK_DOORS"
# Park the vehicle
CMD_PARK = "PARK"
# Park the vehicle in a safe place that is configured for the vehicle
CMD_PARK_IN_SAFE_PLACE = "PARK_IN_SAFE_PLACE"
# Turn on the vehicle’s headlights
CMD_TURN_ON_HEADLIGHTS = "TURN_ON_HEADLIGHTS"
# Turn off the vehicle’s headlights
CMD_TURN_OFF_HEADLIGHTS = "TURN_OFF_HEADLIGHTS"
# Turn on the vehicle’s parking lights, also known as sidelights
CMD_TURN_ON_PARKING_LIGHTS = "TURN_ON_PARKING_LIGHTS"
# Turn off the vehicle’s parking lights, also known as sidelights
CMD_TURN_OFF_PARKING_LIGHTS = "TURN_OFF_PARKING_LIGHTS"
# Accelerate the vehicle, that is, press the gas pedal
CMD_ACCELERATE = "ACCELERATE"
# Brake the vehicle, that is, press the brake pedal
CMD_BRAKE = "BRAKE"
# Make the vehicle rotate to the right. We must specify the degrees 
# we want the vehicle to rotate right in the value for the DEGREES key
CMD_ROTATE_RIGHT = "ROTATE_RIGHT"
# Make the vehicle rotate to the left. We must specify the degrees 
# we want the vehicle to rotate left in the value for the DEGREES key
CMD_ROTATE_LEFT = "ROTATE_LEFT"
# Set the maximum speed that we allow to the vehicle. We must specify 
# the desired maximum speed in miles per hour in the value for the MPH key
CMD_SET_MAX_SPEED = "SET_MAX_SPEED"
# Set the minimum speed that we allow to the vehicle. We must specify 
# the desired minimum speed in miles per hour in the value for the MPH key
CMD_SET_MIN_SPEED = "SET_MIN_SPEED"
# Degrees key
KEY_DEGREES = "DEGREES"
# Miles per hour key
KEY_MPH = "MPH"

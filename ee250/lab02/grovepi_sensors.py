""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Joshua Williams

Insert Github repository link here.
https://github.com/jwills15/GrovePi-EE250/tree/lab02
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd

### Setup for Ultrasonic Sensor
# Connect the Grove Ultrasonic Ranger to digital port D4
ultrasonic_ranger_PORT = 4

### Setup for Rotatry Angle Sensor
# Connect the Grove Rotary Angle Sensor to analog port A0
potentiometer_PORT = 0
grovepi.pinMode(potentiometer_PORT,"INPUT")
# Reference voltage of ADC is 5v
adc_ref = 5
# Vcc of the grove interface is normally 5v
grove_vcc = 5
# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

### Setup for LCD
green = [0, 128, 0]
red = [255, 0, 0]
object_detected_string = "OBJ PRES"

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        # Read sensor value from potentiometer and potentiometer
        potentiometer_value = grovepi.analogRead(potentiometer_PORT)      
        ultrasonic_value = grovepi.ultrasonicRead(ultrasonic_ranger_PORT)

        # Format values for display on LCD
        string_output = str(potentiometer_value).rjust(4, ' ') + "cm"
        
        color_output = green
        if potentiometer_value > ultrasonic_value:
            color_output = red
            string_output = string_output + " " + object_detected_string
        else:
            # needed to use the non-flickering version of lcd.setText
            string_output = string_output + "         "

        string_output = (string_output + "\n" + 
                str(ultrasonic_value).rjust(4, ' ') + "cm")

        # Display on LCD
        grove_rgb_lcd.setText_norefresh(string_output)
        grove_rgb_lcd.setRGB(color_output[0], color_output[1], color_output[2])
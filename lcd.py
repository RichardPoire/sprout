import time

import Adafruit_CharLCD as LCD

# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

# LED color

#Red Connection lost WU
lcd.set_color(1.0, 0.0, 0.0)
time.sleep(1.0)

#Green Status OK
lcd.set_color(0.0, 1.0, 0.0)
time.sleep(1.0)

#Blue Watering in progress (GPIO active)
lcd.set_color(0.0, 0.0, 1.0)
time.sleep(1.0)

#Yellow Will not water today (Rain > xx mm)
lcd.set_color(1.0, 1.0, 0.0)
time.sleep(1.0)

#Cyan ???
lcd.set_color(0.0, 1.0, 1.0)
time.sleep(1.0)

#Magenta ???
lcd.set_color(1.0, 0.0, 1.0)
time.sleep(1.0)

#White ???
lcd.set_color(1.0, 1.0, 1.0)
time.sleep(1.0)

#LCD message 
lcd.message(Time)



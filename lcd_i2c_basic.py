from machine import SoftI2C, Pin
from machine_i2c_lcd import I2cLcd

i2c = SoftI2C(sda=Pin(9), scl=Pin(8))
lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.putstr("Funciona")
#lcd.putstr("\nè(a^2+b^2) It's alive!")

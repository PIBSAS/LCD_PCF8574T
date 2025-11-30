from machine import I2C, Pin
from time import sleep
from machine import SoftI2C, Pin
from machine_i2c_lcd import I2cLcd




I2C_ADDR = 0x27     # típico del PCF8574
ROWS = 2
COLS = 16

# Configurar I2C (cambiá los pines a tu conexión)
i2c = SoftI2C(sda=Pin(9), scl=Pin(8))

# Crear LCD
#lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)
lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)
# Encender backlight
lcd.backlight_on()

# Loop
while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Se corto internet\n")
    sleep(2)

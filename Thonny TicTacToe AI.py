from machine import Pin,I2C
import mcp23017

i2c = I2C(0, scl=Pin(20), sda=Pin(22))
mcp = mcp23017.MCP23017(i2c, 0x20)

mcp[1].value(0)
mcp[2].value(0)
mcp[3].value(0)
mcp[4].value(0)
mcp[5].value(0)
mcp[6].value(0)
mcp[7].value(0)
mcp[8].value(0)

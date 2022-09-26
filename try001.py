import serial
import minimalmodbus

server = '127.0.0.1'

serialPort = '/dev/serial0'

temperature = None
humidity = None
dhtDTTM = None

_BaudRate = input("enter baud rate");
_DataBits = input("enter databits : ");
_Parity = input("enter parity : ");
_StopBits = input("enter stop bit");

instrument = minimalmodbus.Instrument(serialPort, 1)  # , debug=True
instrument.serial.baudrate = _BaudRate  # Baud
instrument.serial.bytesize = _DataBits
instrument.serial.parity = _Parity  # Parity[_Parity]
instrument.serial.stopbits = _StopBits  # StopBits - 1
instrument.serial.timeout = 1.5

fc= input("enter fc : "); 
reg = input("enter register address: ")
val = instrument.read_register(reg, number_of_decimals=0, functioncode=fc, signed=False)
print(val);





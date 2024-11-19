from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE
from time import sleep

s = Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
    bytesize=EIGHTBITS,
    parity=PARITY_NONE,
    stopbits=STOPBITS_ONE,
    timeout=None,
    xonxoff=True,
    rtscts=False,
    dsrdtr=False,
    write_timeout=None,
    inter_byte_timeout=None,
    exclusive=True,
)


current = open("current", "wb")
history = open("history", "wb")

while True:
    s.write(f"CURVe")
    r = s.readline()
    
    current.seek(0)
    current.truncate(0)
    current.write(r)

    history.write(r + b"\n")

    sleep(1)

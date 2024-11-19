from random import randbytes
from time import sleep

while True:
	with open("current", "wb") as f:
		f.write(randbytes(5000))
	sleep(1)

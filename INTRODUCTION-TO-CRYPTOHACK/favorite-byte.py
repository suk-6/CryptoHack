from Crypto.Util.number import *
from pwn import *

cipher = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
)

for b in cipher:
    print(chr(b ^ 16), end="")

from pwn import *

cipher = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)

origin_key = []

for i in list("crypto{"):
    origin_key.append(cipher[len(origin_key)] ^ ord(i))

count = 0

for i in range(200):
    key = []
    key.extend(origin_key)
    key.append(i)
    k = 0
    flag = ""
    print(key)
    for j in cipher:
        flag += chr(j ^ key[k % len(key)])
        k += 1
    count += 1
    print(str(count) + ": " + flag)

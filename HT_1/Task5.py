# 5. Write a script to convert decimal to hexadecimal
#         Sample decimal number: 30, 4
#         Expected output: 1e, 04

def dec2hex(n):
    return ''.join((hex(n)).split('0x'))

print(dec2hex(30) + ',', dec2hex(4))
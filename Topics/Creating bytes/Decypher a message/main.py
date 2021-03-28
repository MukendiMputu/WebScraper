enc_msg = input()
int_bytecode = int(input()).to_bytes(2, byteorder='little')
byte_sum = 0
for _byte in int_bytecode:
    byte_sum += _byte
dec_msg = ''
for _char in enc_msg:
    dec_msg += chr(ord(_char) + byte_sum)
print(dec_msg)

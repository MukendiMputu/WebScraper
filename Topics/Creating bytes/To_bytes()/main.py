byte_sequence = (int(input())).to_bytes(2, byteorder='little')
sum_of_byte = 0
for _byte in byte_sequence:
    sum_of_byte += _byte
print(sum_of_byte)

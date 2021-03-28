unicode_input = int(input())
# print(chr(unicode_input) if unicode_input in range(32, 127) else False)
if unicode_input in range(32, 127):
    print(chr(unicode_input))
else:
    print(False)

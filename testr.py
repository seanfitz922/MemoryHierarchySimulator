# Address in hexadecimal format
address_hex = 'c84'

# Convert hexadecimal to binary
address_bin = bin(int(address_hex, 16))[2:]  # Convert hexadecimal to binary and remove '0b' prefix

print(address_bin)

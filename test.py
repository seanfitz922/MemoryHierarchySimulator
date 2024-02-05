import math


# page siZw is 256 bytes and there are 64 virtual pages

# offset is log2(pagesize)
page_offset = math.log2(256)
print(page_offset, 'bits')
# virtual page is log2(num_virt_pages)
virtual_page_number = math.log2(64)
print(virtual_page_number, 'bits')



# convert address to binary
# ex: R:c84 ->            1100_1000_0100 
# Page Offset:                 100_0100
# Virtual Page Number:    1100_10
# index:                     0
# Tag:                    110 (6)

# ex: R:81c ->           1000_0001_1100
# Page offset:                001_1100
# Virtual Page Number:   1000_00
# index:                    0
# tag:                   100 (4)



'''
For a direct-mapped TLB with 2 sets:
The index bit is the least significant bit of the VPN (Virtual Page Number).
The TLB tag is formed by the remaining bits of the VPN.
'''


# Cache Size = 4 sets * 1 (set size) * 16 bytes = 64 bytes
# block size = line size
print('-------------------')
# offset
print(math.log2(16), 'bits')
# index
print(math.log2(4), 'bits')
# tag
print(12 - (2+4), 'bits')

# 1100_10|00_|0100 
#   tag  indx  offset

# 1000_00|01_|1100

# 000101|00|1000

# 011101|10|1000
#  4 * 16
# page_offset = 400 % 256
phys_add = (3 * 256) + 0
index = (phys_add % 4)
print(index % 4)
print(phys_add / (4 * 16))
# Physical Page Number * Page Size + Page Offset
# phys / (sets * line size)

# page_offset = 332 % 256
phys_add = (1 * 256) + 8
index = (phys_add % 4)
# print(index % 4)
print(phys_add / (4 * 16))

phys_add = (2 * 256) + 68
print(math.floor(phys_add / (4 * 16)))

# CONVERT HEX TO DECIMAL 84 -> 132
phys_add = (0 * 256) + 132 
print((phys_add / (4 * 16)))

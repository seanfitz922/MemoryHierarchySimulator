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



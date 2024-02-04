import math
from config import read_config, parse_section

def main():
    
    config = read_config()
    data_tlb = parse_section(config['Data TLB configuration'])
    page_table = parse_section(config['Page Table configuration'])
    data_cache = parse_section(config['Data Cache configuration'])
    L2_cache = parse_section(config['L2 Cache configuration'])
    # fix me 
    virtual_addresses = L2_cache

    if {virtual_addresses["TLB"]} == 'y':
        pass

    # TLB
    print(f'Data TLB contains {data_tlb["Number of sets"]} sets.')
    print(f'Each set contains {data_tlb["Set size"]} entries.')
    print(f'Number of bits used for the index is {math.ceil(math.log2(int(data_tlb["Number of sets"])))}. \n')

    # Pages
    print(f'Number of virtual pages is {page_table["Number of virtual pages"]}.')
    print(f'Number of physical pages is {page_table["Number of physical pages"]}.')
    print(f'Each page contains {page_table["Page size"]} bytes.')
    print(f'Number of bits used for the page table index is {math.ceil(math.log2(int(page_table["Number of virtual pages"])))}.')
    print(f'Number of bits used for the page offset is {math.ceil(math.log2(int(page_table["Page size"])))}. \n')

    # DC
    print(f'D-cache contains {data_cache["Number of sets"]} sets.')
    print(f'Each set contains {math.ceil((int(data_cache["Set size"]) * int(data_cache["Number of sets"])) / int(data_cache["Number of sets"]))} entries.')
    print(f'Each line is {data_cache["Line size"]} bytes.')

    if data_cache['Write through/no write allocate'] == 'y':
        print("The cache uses a no write-allocate and write through policy.")
    else:
        print("The cache uses a write-back and FIX ME")

    print(f'Number of bits used for the index is {math.ceil(math.log2(int(data_cache["Number of sets"])))}.')
    print(f'Number of bits used for the offset is {math.ceil(math.log2(int(data_cache["Line size"])))}. \n')

    if virtual_addresses["L2 cache"] == 'y':
        pass
        
    # L2
    print(f'L2-cache contains {L2_cache["Number of sets"]} sets.')
    print(f'Each set contains {math.ceil((int(L2_cache["Set size"]) * int(L2_cache["Number of sets"])) / int(L2_cache["Number of sets"]))} entries.')
    print(f'Each line is {L2_cache["Line size"]} bytes.')
    print(f'Number of bits used for the index is {math.ceil(math.log2(int(L2_cache["Number of sets"])))}')
    print(f'Number of bits used for the offset is {math.ceil(math.log2(int(L2_cache["Line size"])))}.\n')

    if virtual_addresses['Virtual addresses'] == 'y':
        print("The addresses read in are virtual addresses.")
    else:
        print("FIX ME")
        


if __name__ == "__main__":
    # Execute main logic
    main()
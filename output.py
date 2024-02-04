import math

# calculations of index, offset taken from:
# https://stackoverflow.com/questions/66610406/how-to-find-number-of-bits-in-tag-field-of-cache-block
# https://stackoverflow.com/questions/7910240/how-to-calculate-page-table-size

class OutputPrinter:  
    # TLB
    def print_data_tlb_info(data_tlb):
        print(f'Data TLB contains {data_tlb["Number of sets"]} sets.')
        print(f'Each set contains {data_tlb["Set size"]} entries.')
        print(f'Number of bits used for the index is {math.ceil(math.log2(int(data_tlb["Number of sets"])))}. \n')

    # Page table
    def print_page_info(page_table):
        print(f'Number of virtual pages is {page_table["Number of virtual pages"]}.')
        print(f'Number of physical pages is {page_table["Number of physical pages"]}.')
        print(f'Each page contains {page_table["Page size"]} bytes.')
        print(f'Number of bits used for the page table index is {math.ceil(math.log2(int(page_table["Number of virtual pages"])))}.')
        print(f'Number of bits used for the page offset is {math.ceil(math.log2(int(page_table["Page size"])))}. \n')

    # DC
    def print_data_cache_info(data_cache):
        print(f'D-cache contains {data_cache["Number of sets"]} sets.')
        print(f'Each set contains {math.ceil((int(data_cache["Set size"]) * int(data_cache["Number of sets"])) / int(data_cache["Number of sets"]))} entries.')
        print(f'Each line is {data_cache["Line size"]} bytes.')

        if data_cache['Write through/no write allocate'] == 'y':
            print("The cache uses a no write-allocate and write-through policy.")
        else:
            print("The cache uses a write-back and FIX ME")

        print(f'Number of bits used for the index is {math.ceil(math.log2(int(data_cache["Number of sets"])))}.')
        print(f'Number of bits used for the offset is {math.ceil(math.log2(int(data_cache["Line size"])))}. \n')

    # l2
    def print_L2_cache_info(L2_cache):
        print(f'L2-cache contains {L2_cache["Number of sets"]} sets.')
        print(f'Each set contains {math.ceil((int(L2_cache["Set size"]) * int(L2_cache["Number of sets"])) / int(L2_cache["Number of sets"]))} entries.')
        print(f'Each line is {L2_cache["Line size"]} bytes.')
        print(f'Number of bits used for the index is {math.ceil(math.log2(int(L2_cache["Number of sets"])))}')
        print(f'Number of bits used for the offset is {math.ceil(math.log2(int(L2_cache["Line size"])))}.\n')

    # Toggles
    def print_address_info(virtual_addresses):
        if virtual_addresses['Virtual addresses'] == 'y':
            print("The addresses read in are virtual addresses.")
        else:
            print("FIX ME")

    def print_table_header():
        print(f"{'Virtual':8s} {'Virt.':6s} {'Page':4s} {'TLB':6s} {'TLB':3s} {'TLB':4s} {'PT':4s} {'Phys':4s} {'':6s} {'DC':3s} {'DC':4s} {'':6s} {'L2':3s} {'L2':4s}")
        print(f"{'Address':8s} {'Page #':6s} {'Off':4s} {'Tag':6s} {'Ind':3s} {'Res.':4s} {'Res.':4s} {'Pg #':4s} {'DC Tag':6s} {'Ind':3s} {'Res':4s} {'L2 Tag':6s} {'Ind':3s} {'Res.':4s}")
        print(f"{'--------':8s} {'------':6s} {'----':4s} {'------':6s} {'---':3s} {'----':4s} {'----':4s} {'----':4s} {'------':6s} {'---':3s} {'----':4s} {'------':6s} {'---':3s} {'----':4s}")

    def print_table_data(trace_data):
        # adding leading zeros taken from https://ioflood.com/blog/python-zfill/#:~:text=The%20zfill()%20method%20in,the%20actual%20number%20they%20represent.
        for data in trace_data:
            address = data.split(":")[-1].removeprefix('R')
            address_padded = address.zfill(8)
            print(f"{address_padded:>8s} {'0':>6s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s} {'0':>4s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s}")



    def print_sim_stats():
        print("\nSimulation statistics\n")

        print(f'dtlb hits')
        print(f'dtlb misses')
        print(f'dtlb hit ratio\n')

        print(f'pt hits')
        print(f'pt faults')
        print(f'pt hit ratio\n')

        print(f'dc hits')
        print(f'dc misses')
        print(f'dc hit ratio\n')

        print(f'L2 hits')
        print(f'L2 misses')
        print(f'L2 hit ratio\n')

        print(f'Total reads')
        print(f'Writes')
        print(f'Ratio of reads')

        print(f'main memory refs')
        print(f'page table refs')
        print(f'disk refs')
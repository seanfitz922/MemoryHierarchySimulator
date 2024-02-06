import math
from tlb import TLB

# calculations of index, offset taken from:
# https://stackoverflow.com/questions/66610406/how-to-find-number-of-bits-in-tag-field-of-cache-block
# https://stackoverflow.com/questions/7910240/how-to-calculate-page-table-size

class OutputPrinter:  
    # TLB
    def print_data_tlb_info(self, data_tlb):
        print(f'Data TLB contains {data_tlb["Number of sets"]} sets.')
        print(f'Each set contains {data_tlb["Set size"]} entries.')
        print(f'Number of bits used for the index is {math.ceil(math.log2(int(data_tlb["Number of sets"])))}. \n')

    # Page table
    def print_page_info(self, page_table):
        print(f'Number of virtual pages is {page_table["Number of virtual pages"]}.')
        print(f'Number of physical pages is {page_table["Number of physical pages"]}.')
        print(f'Each page contains {page_table["Page size"]} bytes.')
        print(f'Number of bits used for the page table index is {math.ceil(math.log2(int(page_table["Number of virtual pages"])))}.')
        print(f'Number of bits used for the page offset is {math.ceil(math.log2(int(page_table["Page size"])))}. \n')

    # DC
    def print_data_cache_info(self, data_cache):
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
    def print_L2_cache_info(self, L2_cache):
        print(f'L2-cache contains {L2_cache["Number of sets"]} sets.')
        print(f'Each set contains {math.ceil((int(L2_cache["Set size"]) * int(L2_cache["Number of sets"])) / int(L2_cache["Number of sets"]))} entries.')
        print(f'Each line is {L2_cache["Line size"]} bytes.')
        print(f'Number of bits used for the index is {math.ceil(math.log2(int(L2_cache["Number of sets"])))}')
        print(f'Number of bits used for the offset is {math.ceil(math.log2(int(L2_cache["Line size"])))}.\n')

    # Toggles
    def print_address_info(self, virtual_addresses):
        if virtual_addresses['Virtual addresses'] == 'y':
            print("The addresses read in are virtual addresses.\n")
        else:
            print("FIX ME")

    def print_table_header(self):
        print(f"{'Virtual':8s} {'Virt.':6s} {'Page':4s} {'TLB':6s} {'TLB':3s} {'TLB':4s} {'PT':4s} {'Phys':4s} {'':6s} {'DC':3s} {'DC':4s} {'':6s} {'L2':3s} {'L2':4s}")
        print(f"{'Address':8s} {'Page #':6s} {'Off':4s} {'Tag':6s} {'Ind':3s} {'Res.':4s} {'Res.':4s} {'Pg #':4s} {'DC Tag':6s} {'Ind':3s} {'Res':4s} {'L2 Tag':6s} {'Ind':3s} {'Res.':4s}")
        print(f"{'--------':8s} {'------':6s} {'----':4s} {'------':6s} {'---':3s} {'----':4s} {'----':4s} {'----':4s} {'------':6s} {'---':3s} {'----':4s} {'------':6s} {'---':3s} {'----':4s}")

    def calculate_TLB_tag_index(self, virt_address, page_table):
        # binary conversion taken from: https://stackoverflow.com/questions/65022145/convert-binary-to-signed-little-endian-16bit-integer-in-python
        binary_address = bin(int(virt_address, 16))[2:].zfill(12)

        page_offset = binary_address[-1*(math.ceil(math.log2(int(page_table['Page size'])))):]
        virtual_page_number = binary_address[:math.ceil(math.log2(int(page_table['Number of virtual pages'])))]
        TLB_index = virtual_page_number[-1]
        TLB_tag = int(virtual_page_number[:(len(page_offset) - len(virtual_page_number)) +1 ], 2)

        return TLB_tag, TLB_index
    
    # def calculate_DC_tag_index(self, page_table, data_cache):
    #     # phys / (sets * line size)
    #     # phys_address = ((PAGE_NUMBER * int(page_table['Page size'])) + page_offset) 
    #     DC_tag = math.floor(phys_address / (sets * line_size))
    #     DC_index = phys_address % num_sets

    #     return DC_tag, DC_index


    def print_table_data(self, trace_data, page_table, data_tlb, tlb_flag, data_cache):
        # adding leading zeros taken from https://ioflood.com/blog/python-zfill/#:~:text=The%20zfill()%20method%20in,the%20actual%20number%20they%20represent.
        tlb = TLB(int(data_tlb["Number of sets"]), int(data_tlb["Set size"]))
        counter = 0
        for data in trace_data:
            virt_address = data.split(":")[-1].removeprefix('R')
            virt_page_num = int(virt_address, 16) // int(page_table["Page size"])
            result = ''
            if tlb_flag:
                # hit or miss for tlb
                result = "miss"
                if tlb.lookup(virt_page_num) == 1:
                    result = "hit"
                    counter +=1
            address_padded = virt_address.zfill(8)

            TLB_tag, TLB_index = self.calculate_TLB_tag_index(virt_address, page_table)
            #DC_index = self.calculate_DC_tag_index(page_table, data_cache)

            if int(virt_address[1]) == 0 and int(virt_address[2]) == 0:
                print(f"{address_padded:>8s} {virt_address[0]:>6s} {virt_address[1]:>4s} {TLB_tag:>6} {TLB_index:>3s} {result:>4s} {'0':>4s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s}")
            elif int(virt_address[1]) == 0 and int(virt_address[2]) != 0:
                print(f"{address_padded:>8s} {virt_address[0]:>6s} {virt_address[2]:>4s} {TLB_tag:>6} {TLB_index:>3s} {result:>4s} {'0':>4s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s}")
            else:
                print(f"{address_padded:>8s} {virt_address[0]:>6s} {virt_address[1:]:>4s} {TLB_tag:>6} {TLB_index:>3s} {result:>4s} {'0':>4s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s} {'0':>6s} {'0':>3s} {'0':>4s}")

        self.print_sim_stats(counter, len(trace_data))

    def print_sim_stats(self, dtlb_hits, length):
        print("\nSimulation statistics\n")

        print(f'dtlb hits        : {dtlb_hits}')
        print(f'dtlb misses      : {length - dtlb_hits}')
        print(f'dtlb hit ratio   : {dtlb_hits / length:.6f}\n')

        print(f'pt hits          :  ')
        print(f'pt faults        :  ')
        print(f'pt hit ratio     :  \n')

        print(f'dc hits          :  ')
        print(f'dc misses        :  ')
        print(f'dc hit ratio     :  \n')

        print(f'L2 hits          :  ')
        print(f'L2 misses        :  ')
        print(f'L2 hit ratio     :  \n')

        print(f'Total reads      :  ')
        print(f'Writes           :  ')
        print(f'Ratio of read    :  ')

        print(f'main memory refs :  ')
        print(f'page table refs  :  ')
        print(f'disk refs        :')
    
    
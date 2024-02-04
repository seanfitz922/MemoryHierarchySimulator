from config import read_config, parse_section
from trace_ import read_trace
from output import OutputPrinter

def main():
    
    config = read_config()
    data_tlb = parse_section(config['Data TLB configuration'])
    page_table = parse_section(config['Page Table configuration'])
    data_cache = parse_section(config['Data Cache configuration'])
    L2_cache = parse_section(config['L2 Cache configuration'])
    virtual_addresses = L2_cache


    if {virtual_addresses["TLB"]} == 'y':
        pass
    
    # output
    OutputPrinter.print_data_tlb_info(data_tlb)
    OutputPrinter.print_page_info(page_table)
    OutputPrinter.print_data_cache_info(data_cache)
    OutputPrinter.print_L2_cache_info(L2_cache)
    OutputPrinter.print_address_info(virtual_addresses)

    # table
    OutputPrinter.print_table_header()
    OutputPrinter.print_table_data(read_trace())
    # OutputPrinter.print_sim_stats()

if __name__ == "__main__":
    main()
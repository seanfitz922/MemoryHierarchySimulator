
# https://www.geeksforgeeks.org/page-table-entries-in-page-table/

class PageTable:
    def __init__(self, num_virtual_pages, num_physical_pages):
        self.num_virtual_pages = num_virtual_pages
        self.num_physical_pages = num_physical_pages
        self.table = [-1] * num_virtual_pages  # Initialize with -1 indicating not mapped

    def map_page(self, virt_page_num, phys_frame_num):
        # Map the virtual page number to the physical frame number
        if virt_page_num < self.num_virtual_pages:
            self.table[virt_page_num] = phys_frame_num

    def translate_address(self, virt_page_num):
        # Translate a virtual page number to a physical frame number
        if virt_page_num < self.num_virtual_pages:
            phys_frame_num = self.table[virt_page_num]
            if phys_frame_num != -1:
                return phys_frame_num
        return None  # Indicates a page fault or unmapped page

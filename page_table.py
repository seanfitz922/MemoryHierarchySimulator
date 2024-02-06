class PageTable:
    def __init__(self, num_pages):
        self.num_pages = num_pages
        self.table = {}

    def insert_mapping(self, virt_page_num, phys_frame_num):
        self.table[virt_page_num] = phys_frame_num

    def lookup(self, virt_page_num):
        if virt_page_num in self.table:
            return self.table[virt_page_num]
        else:
            # Hnadle fault FIX ME
            return -1


class TLB_Entry:
    def __init__(self, virt_page_num, phys_frame_num):
        self.virt_page_num = virt_page_num
        self.phys_frame_num = phys_frame_num
        self.LRU_counter = 0

# insight gained from https://github.com/lagunetero91/lruTLBSimulator/blob/master/lru.c
       # https://www.geeksforgeeks.org/translation-lookaside-buffer-tlb-in-paging/
class TLB:
    def __init__(self, num_sets, set_size):
        self.num_sets = num_sets
        self.set_size = set_size
        self.entries = []
        for _ in range(num_sets):
            set_entries = []
            for _ in range(set_size):
                entry = TLB_Entry(None, None)
                set_entries.append(entry)
            self.entries.append(set_entries)

    def lookup(self, virt_page_num):
        # Searching for virt page num in TLB
        # https://www.geeksforgeeks.org/python-hash-method/
        # https://stackoverflow.com/questions/60659724/how-does-a-tlb-differ-from-a-hash-table
        for entry in self.entries[hash(virt_page_num) % self.num_sets]:
            if entry.virt_page_num == virt_page_num:
                # Hit (1), Update LRU counter
                max_LRU_counter_in_set = float('-inf')

                # loop through entries find the max LRU counter
                for entry in self.entries[hash(virt_page_num) % self.num_sets]:
                    max_LRU_counter_in_set = max(max_LRU_counter_in_set, entry.LRU_counter)

                # Update the LRU counter for the current entry
                entry.LRU_counter = max(entry.LRU_counter, max_LRU_counter_in_set + 1)                
                return 1

        # Miss (0), Update TLB with new entry and use LRU
        # LRU heavily inspired from :https://www.analyticsvidhya.com/blog/2021/08/caching-in-python-the-lru-algorithm/
        min_LRU_entry = None
        # taken from https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
        min_LRU_counter = float('inf')
        
        hash_value = hash(virt_page_num) % self.num_sets

        for entry in self.entries[hash_value]:
            if entry.LRU_counter < min_LRU_counter:
                min_LRU_counter = entry.LRU_counter
                min_LRU_entry = entry

        # Update the min lrU entry
        min_LRU_entry.virt_page_num = virt_page_num

        # Update the LRU counter
        max_LRU_counter = float('-inf')

        for entry in self.entries[hash_value]:
            max_LRU_counter = max(max_LRU_counter, entry.LRU_counter)

        min_LRU_entry.LRU_counter = max_LRU_counter + 1

        return 0

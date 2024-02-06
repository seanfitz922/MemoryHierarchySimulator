class TLBEntry:
    def __init__(self, vpn, pfn):
        self.vpn = vpn
        self.pfn = pfn
        self.lru_counter = 0

class TLB:
    def __init__(self, num_sets, set_size):
        self.num_sets = num_sets
        self.set_size = set_size
        self.entries = [[TLBEntry(None, None) for _ in range(set_size)] for _ in range(num_sets)]

    def lookup(self, vpn):
        # Search for the virtual page number in the TLB
        for entry in self.entries[hash(vpn) % self.num_sets]:
            if entry.vpn == vpn:
                # Hit: Update LRU counters and return 1
                entry.lru_counter = max(entry.lru_counter, max(entry.lru_counter for entry in self.entries[hash(vpn) % self.num_sets]) + 1)
                return 1

        # Miss: Update TLB with new entry and apply LRU replacement policy
        min_lru_entry = min(self.entries[hash(vpn) % self.num_sets], key=lambda entry: entry.lru_counter)
        min_lru_entry.vpn = vpn
        min_lru_entry.lru_counter = max(entry.lru_counter for entry in self.entries[hash(vpn) % self.num_sets]) + 1

        return 0

# Example usage with the given configuration
tlb = TLB(num_sets=2, set_size=1)
virtual_addresses = ["c84", "81c", "14c", "c84", "400", "148", "144", "c80", "008"]

for address in virtual_addresses:
    vpn = int(address, 16) // 256  # Extract virtual page number
    result = tlb.lookup(vpn)
    print(f"Virtual Address: {address}, TLB Result: {result}")

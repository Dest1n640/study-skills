class MemoryStore:
    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)
        return len(self.orders)

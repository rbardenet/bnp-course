class Counter:
    "This is a counter class"
    def __init__(self):
        self.value = 0

    def increment(self):
        "Increments the counter"
        self.value = self.value + 1
        
    def decrement(self):
        "Decrements the counter"
        self.value = self.value - 1
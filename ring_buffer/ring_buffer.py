class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.counter = 0

  def append(self, item):
    remainder = self.counter % self.capacity
    self.storage[remainder] = item
    self.counter +=1

  def get(self):
    return [x for x in self.storage if x is not None]
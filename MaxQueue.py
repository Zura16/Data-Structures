from SLLQueue import SLLQueue
from DLLDeque import DLLDeque

class MaxQueue(SLLQueue):

    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x: object):
        SLLQueue.add(self, x)
        while self.max_deque.size() > 0 and x > self.max_deque.get(self.max_deque.size() - 1):
            self.max_deque._remove(self.max_deque.get_node(self.max_deque.size() - 1))
        self.max_deque.add_last(x)

    def remove(self) -> object:
      r = SLLQueue.remove(self)
      if self.max_deque.size() > 0:
        if r == self.max_deque.get(0):
          self.max_deque.remove(0)
      return r

    def max(self):
        if self.max_deque.size() == 0:
            return None
        return self.max_deque.get(0)
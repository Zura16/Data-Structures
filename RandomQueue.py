import numpy as np
import random
from Interfaces import Queue
import ArrayQueue



class RandomQueue(Queue):
  def __init__(self):
    self.queue = ArrayQueue.ArrayQueue()


    '''
__init__: Initialize the state (array, n and j).
'''
    self.n = 0
    self.j = 0


  def add(self, x: object):
    '''
        add: Add the value x to the Queue
        Inputs:
            x: Object type, i.e., any object
    '''
    self.queue.add(x)
    return True

  def remove(self) -> object:
    '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
    if self.queue.n <= 0:
      raise IndexError()
    b = self.queue.new_array(len(self.queue.a))
    i = random.randint(0, len(b)-1)
    for z in range(0, len(b)):
      if z == i:
        continue
      elif z > i:
        b[z - 1] = self.queue.a[z]
      else:
        b[z] = self.queue.a[z]
    self.queue.a = b
    self.queue.n -= 1
    if i == 0:
      self.queue.j = (self.queue.j + 1) % len(self.queue.a)

    if len(self.queue.a) >= 3 * self.queue.n:
      self.queue.resize()
    return self.queue.a

  def size(self) -> int:
    return self.queue.size()


# if __name__ == '__main__':
#      h = RandomQueue()
#      h.add(0)
#      h.add(2)
#      h.add(1)
#      h.add(3)
#      h.remove()
#      h.remove()
#      h.remove()
#      h.remove()
#      print(h.queue.a)
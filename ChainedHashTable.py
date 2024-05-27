from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):

  class Node():
    def __init__(self, key, value):
      self.key = key
      self.value = value

  def __init__(self, dtype=DLList):
    self.dtype = dtype
    self.d = 1
    self.t = self.alloc_table(2**self.d)
    self.z = 193759204821
    self.w = 31
    self.n = 0

  def alloc_table(self, n: int):
    t = np.zeros(n, dtype=object)
    for i in range(n):
      t[i] = self.dtype()
    return t

  def _hash(self, key: int) -> int:
    return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

  def size(self) -> int:
    return self.n

  def find(self, key: int) -> object:
    if key == None:
      return IndexError()
    for i in range(self.t[self._hash(key)].size()):
      if self.t[self._hash(key)][i].key == key:
        return self.t[self._hash(key)][i].value
    return None

  def add(self, key: int, value: object):
    if self.find(key) != None:
      return False
    if self.n == len(self.t):
      self.resize()
    self.t[self._hash(key)].add(0, self.Node(key, value))
    self.n = self.n + 1
    return True



  def remove(self, key: int) -> object:
    hash_value = self._hash(key)
    for i in range(self.t[hash_value].size()):
        if self.t[hash_value][i].key == key:
            removed_value = self.t[hash_value].remove(i).value
            self.n -= 1
            if len(self.t) >= 3 * self.n:
                self.resize()
            return removed_value
    return None

  def resize(self):
    if self.n == len(self.t):
      self.d += 1
    else:
      self.d -= 1
    a = self.alloc_table(2 ** self.d)
    for j in range(len(self.t)):
      for i in range(self.t[j].size()):
        l = self.t[j]
        u = l.get(i)
        a[self._hash(u.key)].add(0, u)
    self.t = a

  def __str__(self):
    s = "["
    for i in range(len(self.t)):
      for j in range(len(self.t[i])):
        k = self.t[i][j]
        s += str(k.key)
        s += ":"
        s += str(k.value)
        s += ";"
    return s + "]"


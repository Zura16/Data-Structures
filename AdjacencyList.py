"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue



class AdjacencyList(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
    for i in range(self.n):
      self.adj[i] = ArrayList.ArrayList()

  def add_edge(self, i: int, j: int):
    if i < 0 or i >= self.n or j < 0 or j >= self.n:
      raise IndexError()

    if j not in self.adj[i]:
      self.adj[i].append(j)

  def remove_edge(self, i: int, j: int):
    if i < 0 or i >= self.n or j < 0 or j >= self.n:
      raise IndexError()
    for l in range(len(self.adj[i])):
      if self.adj[i].get(l) == j:
        self.adj[i].remove(l)
        return True
    return False

  def has_edge(self, i: int, j: int) -> bool:
    for l in range(len(self.adj[i])):
      if self.adj[i].get(l) == j:
        return True
    return False

  def out_edges(self, i) -> List:
    if i < 0 or i > self.n:
      raise IndexError()
    return self.adj[i]

  def in_edges(self, i) -> List:
    if i < 0 or i > self.n:
      raise IndexError()
    incoming = ArrayList.ArrayList()
    for j in range(self.n):
      if self.has_edge(j, i):
        incoming.append(j)
    return incoming

  def bfs(self, r: int):
    traversal = []
    seen = [False] * self.n
    q = ArrayQueue.ArrayQueue()
    q.add(r)
    traversal.append(r)
    seen[r] = True
    while len(q) != 0:
      current = q.remove()
      neighbors = self.out_edges(current)

      for neighbor in neighbors:
        if not seen[neighbor]:
          traversal.append(neighbor)
          seen[neighbor] = True
          q.add(neighbor)
    return traversal

  def dfs(self, r: int):
    traversal = []
    s = ArrayStack.ArrayStack()
    seen = [False] * self.n
    s.push(r)
    while len(s) != 0:
      i = s.pop()
      if not seen[i]:
        traversal.append(i)
        seen[i] = True
        neighbors = self.out_edges(i)
        for neighbor in reversed(neighbors):
          s.push(neighbor)
    return traversal

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s

  def size(self):
    return self.n


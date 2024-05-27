from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""


class AdjacencyMatrix(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros((self.n, self.n), dtype=int)

  def add_edge(self, i: int, j: int):
    if i < 0 or i > self.n or j < 0 or j > self.n:
      raise IndexError()
    self.adj[i][j] = True

  def remove_edge(self, i: int, j: int):
    if self.adj[i][j]:
      self.adj[i][j] = False
      return True
    else:
      return False

  def has_edge(self, i: int, j: int) -> bool:
    return self.adj[i][j]

  def out_edges(self, i) -> List:
    list = ArrayList.ArrayList()
    for j in range(self.n):
      if self.has_edge(i, j):
        list.append(j)
    return list

  def in_edges(self, i) -> List:
    edges = ArrayList.ArrayList()
    for j in range(self.n):
      if self.has_edge(j, i):
        edges.append(j)
    return edges

  def bfs(self, r: int):
    traversal = []
    seen = [False] * self.n
    q = ArrayQueue.ArrayQueue()
    q.add(r)
    traversal.append(r)
    seen[r] = True
    while len(q) != 0:
      i = q.remove()
      z = self.out_edges(i)

      for t in z:
        if not seen[t]:
          traversal.append(t)
          seen[t] = True
          q.add(t)
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
        z = self.out_edges(i)
        for t in reversed(z):
          s.push(t)
    return traversal

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s

  def size(self):
    return self.n
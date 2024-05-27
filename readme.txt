(Optional) Installation

Install Python 3.8 or higher and numpy. A highly recommended IDE is PyCharm 
https://www.jetbrains.com/pycharm/.

Calculator 

The calculator exemplifies the use of Stacks, HashTables and BinaryTrees. It allows defining mathematical expression with variables, assigning values to the variables and evaluate it.

BookStore

BookStore uses a fraction of the Amazon database to exemplify the use of several data structures
such as Queues, Lists, HashTables, BinarySearch Trees, Heaps, Graphs and sorting. The program
allows adding books to a shopping cart. 

The entry point (main program) is the file main.py. That is done using the 
following lines: 

if __name__ == "__main__":
    main()

To run the program in command line use:

% python3.8 main.py

In Pycharm you can use the otions in the "run" tab.

The program will present the main menu with threee options: 
        1 Calculator
        2 Bookstore System
        0 Exit/Quit
Pressing 1 or 2 and the enter will take you to a second menu with different 
options. The python function that allows to accept an input from the keyboard 
is input(). Use the same pattern to add new options accordingly.

The project is organized in different files (modules):
main.py: The main entry point of the program. It will present the menu that executes the assignments
Calculator.py: The calculator system to be done in Module 2, Module 4 and Module 5
BookStore.py: The book store system to be done during the semester
Book.py: Data class that holds the attributes of a book. The class allows to compare ranks using the operator < or >
SortableBook.py: Data class that holds the attributes of a book. The class allows to compare by alphabetical order using the operator < or >
Interfaces.py: The interfaces to be implemented during the semeter: Stack, Queue, Deque, List, Set, Graph
ArrayStack.py: It will implement the interface Stack in Module 2
ArrayQueue.py: It will implement the interface Queue in Module 2
ArrayList.py: It will implement the interface List in Module 2
ArrayDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of ArrayList
RandomQueue.py: It will implement the interface Queue. It is a specialization (Inheritance) of ArrayQueue
SLLStack.py: It will implement the interface Stack in Module 3
SLLQueue.py: It will implement the interface Queue in Module 3
DLList.py: It will implement the interface List in Module 3
DLLDeque.py: It implements the interface Deque. It is a specialization (Inheritance) of DLLList.
ChainedHashTable.py: It will implement the interface Set in Module 4
BinarySearchTree.py: It will implement the interface Set in Module 5
BinaryHeap.py: It will implement the interface Queue in Module 6. It removes the element with highest priority
algorithms.py: It will implement the sorting algorithms in Module 7
AdjacencyList.py: It will implement the Graph interface in Module 8 using the adjencency list
AdjacencyMatrix.py: It will implement the Graph interface in Module 8 using the adjacency matrix
RedBlackTree.py: It will implement the interface Set a balance tree.  This will be given as an extra-credit assignment, if time permits discussion of the relevant topics.


Stack
    |- ArrayStack
    |- SLLStack     
Queue   
    |- ArrayQueue
            |- RandomQueue
            |- MaxQueue
    |- SLLQueue
    |- BinaryHeap
List                            Dequeue
    |- ArrayList                 |
                |- ArrayDeque   -|
    |- DLList                    |
                |- DLLDeque     -|
Set
    |- ChainedHashTable
    |- BinarySearchTree
Graph
    |- AdjacencyMatrix
    |- AdjacencyList


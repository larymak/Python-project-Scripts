# Union Find (Disjoint Set Union) - Implementation and Use

## Table of Contents
- [Why Union Find?](#why-union-find)
- [Functions and Examples](#functions-and-examples)
- [Setup](#setup)
- [Additional Resources](#additional-resources)
- [Leetcode Questions](#leetcode-questions)

## Why Union Find?
Union Find is a popular data structure that allows us to solve many different types of graph
problems. It works best with undirected graphs, and it allows us to figure out whether a node
is connected to another node.

Some problems it can be used to solve:
- Find the minimum spanning tree in a graph (Kruskal's)
- Check if there is a path between two nodes
- Finding redundant edges 
- Representing networks 


## Functions and Examples
Union Find seems complex at first, but it is actually a lot easier when you understand that there are 
only two functions.
- Find(n) : returns the parent of a node n
- Union(n1, n2) : connects n1 and n2 if they are not previously connected

Let's look at an example!  
```python
u = UnionFind(7)  # create a UnionFind object with 7 nodes (numbered 0 to 6)

u.union(0, 1)     # connects 0 and 1 together
u.union(5, 6)     # connects 5 and 6 together

u.find(1)         # returns 0, since 0 is parent of 1
u.find(5)         # returns 5, since 5 is its own parent

u.union(1, 2)     # connects 2 to the component 0-1
u.find(2)         # 2s parent is now 0

# Now our structure looks like this

# 0-1-2   3  4  5-6

u.union(1, 6)    # first we find the parents of 1 and 6
                 # parents are 0, and 5
                 # connect the smaller component to the bigger
                 # now 5's parent is 0

u.find(6)       # now this goes:
                # 6 parent is 5 -> 5 parent is 0 -> 0 is its own parent
```

And that's it! You can use the sample code to test different examples with Union Find.
In the code, par keeps track of the parent of each node and rank keeps track of the size of 
each component.

## Setup

First clone the repo
 > `cd union_find` to get into this folder.   
 >  call the verify function anywhere, consider adding ``` if __name__ == '__main__'```  
 > `python union_find.py` to run the demo

 You can modify the structure in the verify function and play around with it.

 ## Additional Resources

 Here are some resources I found useful when learning: 
 - Neetcode Graph Videos on YouTube 
 - William Fiset - Union Find Video on YouTube
 - Union Find Medium Article by Claire Lee 
 - Union Find Visualizer - Visualgo 

 ## Leetcode Questions
 - 200 - Number of Islands
 - 684 - Redundant Connection
 - 695 - Max Area of an Island
 - 827 - Making a Large Island 
 - 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
 - 2421 - Maximum Score of a Good Path
 - 2709 - Greatest Common Divisor Traversal 

 I hope this was helpful. If there are any mistakes or issues or if you want to contribute to union find, feel free to contact me at rawateshaan0 [at] gmail [dot] com
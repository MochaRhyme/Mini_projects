import sys

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left = left_node
        self.right = right_node

n=int(sys.stdin.readline())
nodes={}

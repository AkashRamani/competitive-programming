#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class Node: 
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.next = None
        self.prv = None


class LRUCache:
    '''
        Previous verison is the same code, this one is just more organized.

        Time: O(1), Space (1)

        A good explanation is: https://www.youtube.com/watch?v=z9bJUPxzFOw 
        Just watch it for first 5 mintues to understand the solution and there after code is easy
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_set = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prv = self.head

    def remove_node(self, node: Node):
        node.prv.next = node.next
        node.next.prv = node.prv
        return

    def set_as_first_node(self, node: Node):
        node.next = self.head.next
        self.head.next = node

        node.next.prv = node
        node.prv = self.head
        return

    def get(self, key: int) -> int:
        if key in self.hash_set:
            node = self.hash_set[key]
            
            # make this the most recently used, so shift this node as the head of LL
            self.remove_node(node)
            self.set_as_first_node(node)

            return node.value
        return -1   


    def put(self, key: int, value: int) -> None:
        if key in self.hash_set:
            #bring the node to head.. and replace the value
            node = self.hash_set[key]
            node.value = value

            self.remove_node(node)
            self.set_as_first_node(node)

            return None

        if len(self.hash_set) >= self.capacity:
            #remove the least recently used key (right before tail) from LL and from delete that key from hash_set
            node = self.tail.prv
            self.remove_node(node)

            del self.hash_set[node.key]

        #set node as head, then add reference of it to hash_set
        node = Node(key, value)
        self.set_as_first_node(node)
        self.hash_set[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


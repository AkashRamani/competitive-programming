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
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_set = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prv = self.head


    def get(self, key: int) -> int:
        if key in self.hash_set:
            node = self.hash_set[key]
            

            # make this the most recent used, so put this head of LL?

            node.prv.next = node.next
            node.next.prv = node.prv

            node.next = self.head.next
            self.head.next = node

            node.next.prv = node
            node.prv = self.head

            self.hash_set[key] = node

            return node.value


        return -1   

    def put(self, key: int, value: int) -> None:
        if key in self.hash_set:
            #bring the node to head.. and replace the value
            node = self.hash_set[key]

            node.prv.next = node.next
            node.next.prv = node.prv

            node.next = self.head.next
            self.head.next = node

            node.next.prv = node
            node.prv = self.head

            node.value = value
            self.hash_set[key] = node
            return None

        if len(self.hash_set) >= self.capacity:
            #remove the least recently used key (tail) from LL and from delete that key from hash_set
            node_to_delete = self.tail.prv

            self.tail.prv.prv.next = self.tail
            self.tail.prv = self.tail.prv.prv

            del self.hash_set[node_to_delete.key]


        #set node as head, then add reference of it to hash_set
        node = Node(key, value)

        node.next = self.head.next
        self.head.next = node

        node.next.prv = node
        node.prv = self.head

        self.hash_set[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end


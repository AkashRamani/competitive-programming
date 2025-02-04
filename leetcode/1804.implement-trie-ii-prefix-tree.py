class TrieNode:
    def __init__(self):
        self.hash_set = {} 
        self.word_count = 0
        self.prefix_count = 0

    def add_item_to_set(self, key, val): #val is ptr to next node //None aft deletion
        self.hash_set.update({key: val})

    def get_node(self, letter):
        return self.hash_set.get(letter)

    def get_word_count(self):
        return self.word_count

    def get_prefix_count(self):
        return self.prefix_count

    def increment_prefix_count(self):
        self.prefix_count +=1

    def increment_word_count(self):
        self.word_count +=1

    def decrement_prefix_count(self):
        self.prefix_count -=1
    def decrement_word_count(self):
        self.word_count -=1


class Trie:
    '''
        Each operation has a liner time wrt sie of word/ prefix

        Deleting Node when both counts become zero can be a good-on add on
    '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not curr.get_node(letter):
                curr.add_item_to_set(letter, TrieNode())

            curr = curr.get_node(letter)
            curr.increment_prefix_count()
        curr.increment_word_count()

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root

        for letter in word:
            if not curr.get_node(letter):
                return 0
            curr = curr.get_node(letter)
        return curr.get_word_count()

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root

        for letter in prefix:
            if not curr.get_node(letter):
                return 0
            curr = curr.get_node(letter)
        return curr.get_prefix_count()

    def erase(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not curr.get_node(letter):
                return
            
            curr = curr.get_node(letter)
            curr.decrement_prefix_count()
        curr.decrement_word_count()


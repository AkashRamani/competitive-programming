class TimeMap(object):

    def __init__(self):
        self.dictionary = {}

    def findValue(self, timestamp, key):
        array = self.dictionary[key]

        left = 0
        right = len(array) - 1
        result = ""

        while left <= right:
            mid = left + (right-left)//2

            if array[mid][0] <=timestamp: #found a value less tha TS, now lets set mid such tht we find a more closer(yes lesser) value to TS
                result = array[mid][1]
                left = mid+1
            else:
                right = mid-1
        return result

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not key in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self.dictionary:
            return ""
        
        #Run binary search on dictionary[key]
        return self.findValue(timestamp, key)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
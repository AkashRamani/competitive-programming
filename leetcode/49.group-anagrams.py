#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Instead of iterating through string; we can trade off with space complexity. Knowing that there are only small cased english alphabets, we can use it to our advantage..
        # Make an of len 16; store counts of occurances at each index.
        # You can convert it to a string or a tuple and use them as keys to a hash map. <> SOMETHING LIKE a1b3c5 would be even smarter!
        #TIme and Space => O(n*m) 
        group = []
        group_index = -1
        hash_set= {}   #consider using `defaultdict` => For a shorter code
        for index in range(0, len(strs)):
            key = [0 for i in range(26)]
            for char in strs[index]:
                char_index = ord(char) - ord("a")
                key[char_index] = key[char_index] + 1
            key = tuple(key)    #SOMETHING LIKE a1b3c5 would be even smarter for keys!

            if not key in hash_set:
                group.append([])
                group_index = group_index+ 1
                hash_set[key] = group_index
            
            group[hash_set[key]].append(strs[index])
        return group
            
        ##############################
        #This is O(n*n*m). where n:len on List ; m: (max)len of Strings
        # def isAnagram(str1, str2):
        #     if len(str1) != len(str2):
        #         return False

        #     string_hash = {} 
        #     for i in str1:
        #         string_hash[i] = string_hash.get(i, 0) + 1

        #     for i in str2:
        #         if not i in string_hash:
        #             return False
        #         string_hash[i] = string_hash[i] - 1
        #         if string_hash[i] < 1:
        #             del string_hash[i]
        #     return True

        # group = [[strs[0]]]
        # for index in range(1, len(strs)):
        #     str1 = strs[index]
        #     flag = False
        #     for group_index, element in enumerate(group): 
        #         str2 = element[0]
        #         flag = isAnagram(str1, str2)
        #         if flag:
        #             group[group_index].append(str1)
        #             break
        #     if not flag:
        #         group.append([str1])

        # return group

# @lc code=end


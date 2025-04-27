class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i, j = 0, 0

        number = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if not number and abbr[i] == "0":
                    return False
                number = number*10+ int(abbr[i])
                i+=1
            else:
                if number:
                    # increment j
                    j +=number
                    number = 0
                if j < len(word) and abbr[i] != word[j]:
                    return False
                j+=1
                i+=1

        if number:
            j +=number
        if i == len(abbr) and j == len(word):
            return True
        return False

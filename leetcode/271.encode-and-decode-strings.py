class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for string in strs:
            encoded+= str(len(string))+"#"+string
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i= 0
        while i< len(s):
            num = 0
            while s[i] != "#":
                num = num*10 + int(s[i])
                i+=1
            
            start_index = i+1
            end_index = start_index +num
            i=end_index
            strs.append(s[start_index: end_index])
        
        return strs
    
class Codec2:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return str.split("π")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
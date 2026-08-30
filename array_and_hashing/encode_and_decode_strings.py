from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for i in strs:
            encoded += str(len(i))
            encoded += "#"
            encoded += i
        
        return encoded
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        strs = ""
        i = 0
        
        while i < len(s):
            if s[i].isdigit():
                
                length = ""
                while i < len(s):
                    if not s[i].isdigit():
                        length += s[i]
                        break   
                    
                    length += s[i]
                    i += 1
            
                if length.endswith("#"):
                    i += 1
                    
                    for i in range(i, i + int(length[0:-1])):
                        strs += s[i]
                        i += 1
                    
                    decoded.append(strs)
                    strs = ""
            else:
                i += 1
            
        return decoded
    

# Time: O(n * m)
# Space: O(n + m)

obj = Solution()
encoded = obj.encode(["Hello","World"]) 
decoded = obj.decode(encoded)
print(encoded)
print(decoded)

encoded2 = obj.encode(["0"])
decoded2 = obj.decode(encoded2)
print(encoded2)
print(decoded2)
              
            

            
                    
                
                
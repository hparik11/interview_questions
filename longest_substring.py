import numpy as np


def lengthOfLongestSubstring(string: str) -> int:
    hashMap = {}
    i = 0
    maxLen = 0
    for ch in string:
        if(ch in hashMap):
            maxLen = max(maxLen, i)
            i=0
        else:
            i+=1
            hashMap[ch] = True
    
    print(hashMap)
    print(maxLen)

        

if __name__ == "__main__":
    lengthOfLongestSubstring("abcdaeab")
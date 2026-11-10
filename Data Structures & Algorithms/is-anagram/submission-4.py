class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_first = {}
        for i in s:
            if i in dictionary_first:
                dictionary_first[i] +=1
            else:
                dictionary_first[i] = 1
        dictionary_second = {}
        for i in t:
            if i in dictionary_second:
                dictionary_second[i] +=1
            else:
                dictionary_second[i] = 1

        if len(dictionary_first) != len(dictionary_second):
                return False
                
        for i, j in dictionary_first.items():
            if i not in dictionary_second:
                return False

            if j != dictionary_second[i]:
                return False

        return True
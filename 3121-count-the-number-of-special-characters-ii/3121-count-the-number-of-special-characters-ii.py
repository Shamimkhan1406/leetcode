class Solution(object):
    def numberOfSpecialChars(self, word):
        dic={}
        count = 0
        for i in range(len(word)):
            if word[i].isupper() and word[i] not in dic:
                dic[word[i]] = i
            if word[i].islower():
                dic[word[i]] = i
        for k,v in dic.items():
            if k.lower() in dic and dic[k.lower()] < v:
                count += 1
        return count
        """
        :type word: str
        :rtype: int
        """
        
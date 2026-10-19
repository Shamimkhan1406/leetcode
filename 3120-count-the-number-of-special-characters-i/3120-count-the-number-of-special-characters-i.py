class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0
        s = set()
        for i in range(len(word)):
            if word[i].isupper() and word[i].lower() in word and word[i] not in s:
                count += 1
                s.add(word[i])
        return count
        """
        :type word: str
        :rtype: int
        """
        
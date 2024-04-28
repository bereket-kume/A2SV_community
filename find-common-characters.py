class Solution:
    def commonChars(self, words):
        com = set(words[0])
        for word in words[1:]:
            com = com.intersection(set(word))
        return list(com)

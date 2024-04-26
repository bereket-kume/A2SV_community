class Solution:
    def similarPairs(self, words: List[str]) -> int:
        myset = []
        for word in words:
            myset.append("".join(list((set(sorted(word))))))
        mydict = {}
       
        for i in myset:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        print(mydict)
        count = 0
        for i,j in mydict.items():
            if j > 1 and j < 3:
                count += 1
            elif j == 3:
                count += j
            elif j > 2:
                count += (j/2)*(j-1)
        return int(count)

class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
           return False
        if x < 10:
            return True
        
        r_num = 0
        c_num = x
        while c_num > 0:
            r_num = (r_num * 10) + (c_num % 10)
            c_num //= 10
        return r_num == x

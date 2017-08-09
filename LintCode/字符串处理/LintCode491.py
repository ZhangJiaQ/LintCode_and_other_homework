# 字符串置换 
# 给定两个字符串，请设计一个方法来判定其中一个字符串是否为另一个字符串的置换。
# 置换的意思是，通过改变顺序可以使得两个字符串相等。
# 样例
# "abc" 为 "cba" 的置换。
# "aabc" 不是 "abcc" 的置换。

# 解题思路：将两个字符串排序后，在进行比对，相同则返回True

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        
        if sorted(s) == sorted(t):
            return True
        else:
            return False
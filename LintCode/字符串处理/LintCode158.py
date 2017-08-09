# 两个字符串是变位词 
# 写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。

# 样例
# 给出 s = "abcd"，t="dcab"，返回 true.
# 给出 s = "ab", t = "ab", 返回 true.
# 给出 s = "ab", t = "ac", 返回 false.

# 解题思路：将两个字符串进行排序，然后进行比对，相同则返回True

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
旋转字符串 
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

样例
对于字符串 "abcdefg".
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

解题思路：求出偏移量，利用切片操作，完成旋转字符串

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s == None:
            return None
        n = len(s)
        offset = offset % n
        f = n - offset
        return s[f:n] + s[0:f]
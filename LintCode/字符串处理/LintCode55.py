比较字符串 
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

样例
给出 A = "ABCD" B = "ACD"，返回 true
给出 A = "ABCD" B = "AABC"， 返回 false

解题思路：建立一个字典，先统计字符串A中所有字母出现过的次数
		  然后B中如果出现字典中不存在的字符，返回False
		  每出现A中存在的字符时，字典对应值-1，小于零返回False

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(B) > len(A):
            return False
        if len(B) == 0:
            return True

        d = {}

        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for j in B:
            if j not in d:
                return False
            else:
                d[j] -= 1
                if d[j] < 0:
                    return False

        return True
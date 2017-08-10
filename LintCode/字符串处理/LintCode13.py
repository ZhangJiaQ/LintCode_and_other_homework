# 字符串查找 
# 对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

# 样例
# 如果 source = "source" 和 target = "target"，返回 -1。
# 如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1

# 解题思路：1）先开始遍历source字符串，从开始开始遍历，如果遇到第i个字符加上target的长度大于souce的长度时，停止遍历return -1
          # 2）在遍历的过程中，遇到source第i个字符与target第1个[0]字符相同时，进入对target的遍历
		  # 3）开始遍历target字符串，设置相同字符长度变量n，每当source[i+j]与target[j]相同时，n+=1，当n与target长度相同时，则存在target在source内
		  # 4）return i
		 

class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if len(source) == 0 and len(target) != 0:
            return -1
        if len(source) == 0 and len(target) == 0:
            return 0
        if len(target) == 0:
            return 0
        for i in range(len(source)):
            if i + len(target) > len(source):
                return -1
            else:
                if source[i] == target[0]:
                    n = 0
                    for j in range(len(target)):
                        if target[j] == source[i+j]:
                            n += 1
                        else:
                            break
                    if n == len(target):
                        return i
        return -1
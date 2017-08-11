最长单词 
给一个词典，找出其中所有最长的单词。

样例
在词典
{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]
在词典
{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]

解题思路：设置一个数组，将第一个单词加入，并计算第一个单词的长度
		  计算剩下单词的长度，如果与第一个单词相等加入数组，如果大于第一个单词的长度则清空数组，加入新的单词，重新计算单词长度
		  返回数组

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        m = len(dictionary)
        result = []
        if m == 0:
            return result
        dictlen = len(dictionary[0])
        result.append(dictionary[0])
		
        for i in range(1, m):
            tmp = dictionary[i]
            if len(tmp) == dictlen:
                result.append(tmp)
            elif len(tmp) > dictlen:
                result = []
                dictlen = len(tmp)
                result.append(tmp)
        return result
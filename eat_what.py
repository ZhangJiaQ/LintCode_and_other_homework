#coding:utf-8
import time
import random
def eat_what():
	menu = [u'肉夹馍+凉皮', u'外卖黄焖鸡', u'胡辣汤+包子', u'外卖盖饭', u'山西面馆', u'重庆小面', 
	u'汉堡可乐', u'炸酱面']
	eat = menu[random.randint(0, len(menu)-1)]
	print u'今天吃%s' % eat
	time.sleep(10)
	
if __name__ == '__main__':
	eat_what()
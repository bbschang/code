#-*- coding:utf-8-*-
import jieba
from collections import Counter

#完整演示了制作一个词云的过程

#从文件中读取文本，并使用jieba类将文本序列化
def gettext(filename):
	text = ''
	with open(filename) as fin:
	     for line in fin.readlines():
	         line = line.strip('\n')
	         text += '//'.join(jieba.cut(line))
	         text += '//'
	return text




#从词云来序列化文本
def getciyun(str):
	return jiba.cut(str)

#计算序列化文化的词频
def getcountciyun(str):
	data = dict(Counter(str))
	return data

#按照词频排序

def sortdic(dict):
	s = dict.items()
	return sorted(s,key = lambda b:b[1])

#绘制词云

def draw():
	pass

def main():
	text = gettext('lcs.txt')
	count_text = getcountciyun(text)
	sort_text = sortdic(count_text)
	print len(text),len(count_text),len(sort_text)
	


if __name__ =="__main__":
	main()

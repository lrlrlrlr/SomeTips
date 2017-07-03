s='请把我替换掉!而我不用替换!'


def func1(s):
	tmp=list(s)
	tmp[2]='xx'
	s2=''.join(tmp)
	print(s2)


def func2(s):
	s=s[:2]+'xx'+s[3:]
	print(s)


def func3(s):
	import re
	re.match(r'我').groups()


if __name__=='__main__':
	func1(s)
	func2(s)

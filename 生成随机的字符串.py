import random

def randomname(length=(8,12)):
	def randomchar():#生成随机英文小写
		return chr(random.randint(97,122))
	def randomnum():
		return random.randint(0,9)

	name=''
	for i in range(random.randint(*length)):
		if random.randint(0,1)==0:
			name+=randomchar()
		else:
			name+=str(randomnum())
	return name



def randomname2(length=(8,12)):
	s='qwertyuiopasdfghjklzxcvbnm1234567890'
	result=''.join(random.choices(s,k=random.randint(*length)))
	return result

if __name__ == '__main__':
    print(randomname())
    print(randomname2())
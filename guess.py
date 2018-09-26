

import random

r = random.randint(1, 100)
while True:
	num = input('請輸入一個1~100的整數: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		break
	elif num < r:
		print('比這個大')
	elif num > r:
		print('比這個小')
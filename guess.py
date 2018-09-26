

import random

r = random.randint(1, 100)
i = 0
while True:
	num = input('請輸入一個1~100的整數: ')
	num = int(num)
	i += 1
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', i, '次')
		break
	elif num < r:
		print('比這個大')
	elif num > r:
		print('比這個小')
	print('這是你猜的第', i, '次')
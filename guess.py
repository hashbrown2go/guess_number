import random

start = int(input('請輸入起始值:'))
end = int(input('請輸入結束值:'))
r = random.randint(start, end)
i = 0
while True:
	num = input('輸入一個數字: ')
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
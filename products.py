#products

products = []
while True:
	name = input('請輸入商品')
	
	if name == "q": #quit
		break
	price = input('請輸入價格')

	products.append([name, price])

for p in products:
	print(p[0], '的價格是', p[1])
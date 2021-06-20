#products

products = []
while True:
	name = input('請輸入商品: ')
	
	if name == "q": #quit
		break
	price = input('請輸入價格: ')

	products.append([name, price])

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

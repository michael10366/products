#products

products = []
while True:
	name = input('請輸入商品')
	
	if name == "q": #quit
		break
	price = input('請輸入價格')

	products.append([name, price])

print(products)
print(products[0][0])
print(products[0][1])
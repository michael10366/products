#products

#讀取檔案
products = []

with open('products.csv', 'r', encoding = 'UTF-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#使用者書輸入		
while True:
	name = input('請輸入商品: ')
	
	if name == "q": #quit
		break
	price = input('請輸入價格: ')

	products.append([name, price])

#印出商品
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

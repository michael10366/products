#products
import os


#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'UTF-8') as f: 
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products


#使用者書輸入	
def user_input(products):	
	while True:
		name = input('請輸入商品: ')
		if name == "q": #quit
			break
		price = input('請輸入價格: ')
		products.append([name, price])
	return products

#印出商品
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_files(filename, products):
	with open(filename, 'w', encoding = 'UTF-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main(filename):
	if os.path.isfile(filename): #檢查檔案
		print('找到檔案')
		products = read_file(filename)
	else:
		print('沒有檔案')

	
	products = user_input(products)
	print_products(products)
	write_files('products.csv', products)



main('products.csv')
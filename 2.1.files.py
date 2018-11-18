cook_book = {}
bbb = []
with open('recipe_book.txt') as f:
	for line in f:
		name = line.strip()
		number = f.readline().strip()
		for ing in range(int(number)):
			ing = f.readline().strip()
			a = []
			a.append(ing.split(' | '))
			aaa = {'ingridient_name': a[0][0],'quantity': int(a[0][1]), 'measure': a[0][2]}
			bbb.append(aaa)
		
		f.readline()
	cook_book[name] = bbb
print(cook_book)
	


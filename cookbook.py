def add_food(quantity):
	cook_book = {}
	with open('recipes.txt', encoding='utf-8') as file:
		for i in range(quantity):
			name = file.readline().strip()
			cook_book[name] = []
			for k in range(int(file.readline())):
				dish = file.readline().split('|')
				cook_book[name].append({'ingredient_name': dish[0], 'quantity': int(dish[1]), 'measure': dish[2].strip()})
			file.readline()
	return print(cook_book)

add_food(4)
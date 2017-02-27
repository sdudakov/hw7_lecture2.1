# cook_book = {
#   'яйчница': [
#     {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#   'стейк': [
#     {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#     {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},    
#     {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#   'салат': [
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},    
#     {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#     {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
#   }

#Внутри функции записывайте cook_book[dish.strip()] = dict({<словарь-ингредиент>})



def load_cook_book():
	cook_book = {}
	with open("data_hw7.txt", "r", encoding="utf-8") as f:
		for dish in f:
			ingridient_count = int(f.readline())
			# print("dish = {}ingridient_count = {}" .format(dish, ingridient_count))
			for _ in range(ingridient_count):
				ingridient = f.readline()
				ingridient = ingridient.strip()
				ingridient = ingridient.split(" | ")			
			cook_book[dish.strip()] = dict({"ingridient_name": ingridient[0], "quantity": ingridient[1], "measure": ingridient[2]})
	return cook_book

cook_book = load_cook_book()
print(cook_book)

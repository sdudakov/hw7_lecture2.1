def load_cook_book():
	cook_book = {}
	with open("data_hw7.txt", "r", encoding="utf-8") as f:
		for dish in f:
			ingridient_count = int(f.readline())
			ingridient_list = [] #создаю пустой список, который будет обнуляться на следующей итерации
			for _ in range(ingridient_count):
				ingridient = f.readline()
				ingridient = ingridient.strip()
				ingridient = ingridient.split(" | ")
				ingridient_list.append(dict({"ingridient_name": ingridient[0], "quantity": int(ingridient[1]), "measure": ingridient[2]})) #на каждой итерации добавляю в список словарь
			cook_book[dish.strip()] = ingridient_list #присваиваю ключу dish словаря cook_book значение - список, состоящий из словарей
	return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):  
  # for shop_list_item in shop_list.values():
  #   print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    
def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

cook_book = load_cook_book()  
create_shop_list()


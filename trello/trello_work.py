import sys
import requests

FILENAME = "/token.txt"
# открываем скрытый файл на чтение
fd = open(FILENAME, encoding="UTF-8")
#  сохраняем строки этого файла
text_lines = fd.readlines()
# закрываем файл
fd.close()
key_name = text_lines[4]
token_name = text_lines[7]
board_id = text_lines[10]
if "\n" in key_name:
    key_name = key_name[:-1]
if "\n" in token_name:
    token_name = token_name[:-1]
if "\n" in board_id:
    board_id = board_id[:-1]

auth_params = {
    "key": key_name,
    "token": token_name
    }

base_url = "https://api.trello.com/1/{}"

def read():
    # Получим данные всех колонок на доске:      
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()      
    # Теперь выведем название каждой колонки и всех заданий, которые к ней относятся:
    for column in column_data:
        # Получим данные всех задач в колонке и перечислим все названия      
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        print(column['name'] + " - " + str(len(task_data)))
        if not task_data:      
            print('\t' + 'Нет задач!')      
            continue      
        for task in task_data:
            print('\t' + task['name'])


def create_list(column_name):
    # Создает новые колонки
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    column_set = False
    for column in column_data:
        if column_name == column["name"]:
            print("Такая колонка уже есть")
            column_set = True
            break
    if column_set == False:
            requests.post(base_url.format('boards') + '/' + board_id + '/lists', data={'name': column_name, **auth_params})


def delete_list(column_name):
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()
    column_set = False
    for column in column_data:
        if column_name == column["name"]:
            column_set = True
            column_id = column['id']

    if column_set == True:
        requests.delete(base_url.format('boards') + '/' + board_id + '/' + column_id, data={'id': column_id, **auth_params})






def create(name, column_name):      
    # Получим данные всех колонок на доске      
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()      
      
    # Переберём данные обо всех колонках, пока не найдём ту колонку, которая нам нужна      
    for column in column_data:      
        if column['name'] == column_name:      
            # Создадим задачу с именем _name_ в найденной колонке      
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

def delete(name, column_name):
    # Получим данные всех колонок на доске    
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()    
    # Среди всех колонок нужно найти задачу по имени и получить её id    
    task_id = None    
    for column in column_data:
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()    
        for task in column_tasks:    
            if task['name'] == name and column_name == column['name']:
                task_id = task['id']    
                requests.delete(base_url.format('cards') + '/' + task_id, data={'value': task_id, **auth_params})            
                break       
        if task_id:
            break


def move(name, column_name):    
    # Получим данные всех колонок на доске    
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()    
        
    # Среди всех колонок нужно найти задачу по имени и получить её id    
    task_id = None    
    for column in column_data:    
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()    
        for task in column_tasks:    
            if task['name'] == name:    
                task_id = task['id']    
                break    
        if task_id:    
            break    
       
    # Теперь, когда у нас есть id задачи, которую мы хотим переместить    
    # Переберём данные обо всех колонках, пока не найдём ту, в которую мы будем перемещать задачу    
    for column in column_data:    
        if column['name'] == column_name:    
            # И выполним запрос к API для перемещения задачи в нужную колонку    
            requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column['id'], **auth_params})    
            break  





if __name__ == "__main__":    
    if len(sys.argv) <= 2:    
        read()    
    elif sys.argv[1] == 'create':    
        create(sys.argv[2], sys.argv[3])    
    elif sys.argv[1] == 'move':    
        move(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'delete':
        delete(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'create_list':
        create_list(sys.argv[2])
    elif sys.argv[1] == 'delete_list':
        delete_list(sys.argv[2])
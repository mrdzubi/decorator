from datetime import datetime
from list import nested_list

FILE_PATH = 'logs.txt'

def path(path):
    def logger(old_function):
        def data(*args,**kwargs):
            data_time = datetime.now()
            name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open('logs.txt','w', encoding='utf-8') as f:
                f.write(f'Дата: {data_time}\n'
                        f'Функция: {name}\n'
                        f'Переменные: {args,kwargs}\n'
                        f'Результат: {result}\n'
                        f'_______________________________')
            return result
        return data
    return logger

@path(FILE_PATH)
def flat_generator(list):
    for iterlist in list:
        for item in iterlist:
            yield item

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)



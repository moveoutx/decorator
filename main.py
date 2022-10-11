import requests
import os
from datetime import datetime


def logger(l_path=None):
    if l_path is None:
        destination = os.path.join(os.getcwd())
    else:
        destination = os.path.join(os.path.abspath(l_path))
    f_name = 'log_info.txt'
    l_path = os.path.join(destination, f_name)

    def _logger(hero_request):

        def new_function(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = hero_request.__name__
            input_data = f'Данные на входе:{args} и {kwargs}'
            output_data = hero_request(*args, **kwargs)
            result_line = f'Функция: {func_name}\n' \
                          f'Дата и время вызова: {log_date}\n' \
                          f'{input_data} \n'\
                          f'Результат работы: {output_data}\n' \
                          f'##############################################################\n'

            with open(l_path, 'a', encoding='utf-8') as f:
                f.write(result_line)

            return output_data

        return new_function

    return _logger


@logger(input("Введите путь для сохранения лога:"))
def hero_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    intelligence = 0
    hero_name = ''
    for record in response.json():
        if record['name'] == 'Thanos':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']
        if record['name'] == 'Hulk':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']
        if record['name'] == 'Captain America':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']

    print(f'Самый умный герой: {hero_name}')
    print(f'Уровень интеллекта: {intelligence}')
    return hero_name


hero_request()

import csv
import re


def read_file_csv(file_name: str) -> tuple:
    ''' Функция считывает данные из файла .csv, возвращает кортеж, первый элемент которого - список заголовков,
        второй элемент - список с данными людей.
    '''
    with open(file_name, 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
        columns = data[0]
        del data[0]
        return columns, data


def create_number(number: str) -> str:
    ''' Функция принимает один аргумент - номер телефона в произвольном формате.
        Функция возвращает номер телефона в требуемом формате.
    '''

    add_number = None
    if 'доб' in number:
        number, add_number = number.lower().split('доб')
    result = re.findall(r'\d', number)
    result = '+7(' + ''.join(result[1:4]) + ')' + ''.join(result[4:7]) + \
        '-' + ''.join(result[7:9]) + '-' + ''.join(result[9:])
    if add_number:
        add_number = re.search('\d+', add_number)
        result += ' доб.' + add_number[0]
    return result


def create_adress_book(data: list[list]) -> dict:
    ''' Функция принимает один аргумент - список списков, в каждом из которых данные человека.
        Функция приводит данные к требуемому формату, объединяет данные одного и того же человека.
        Функция возращает словарь, содержащий данные людей.
    '''

    data_dict = {}
    for human in data:
        full_name = ' '.join(human[:3])
        full_name = [element for element in full_name.split(' ') if element]
        human_name = ' '.join(full_name[:2])
        if human_name not in data_dict:
            data_dict[human_name] = []
            data_dict[human_name].append(
                full_name[2] if len(full_name) == 3 else '')
            data_dict[human_name].extend(human[3:])
        else:
            data_dict[human_name][2] = human[2] if human[2] else data_dict[human_name][2]
            for index, element in enumerate(human[3:]):
                data_dict[human_name][index +
                                      1] = element if element else data_dict[human_name][index+1]
    for human_name in data_dict:
        data_dict[human_name][3] = create_number(data_dict[human_name][3])
    return data_dict


def write_file_csv(file_name: str, columns: list[str], data: dict):
    '''Функция выводит производит запись в файл данных людей.
       Параметры: file_name - имя файла, в который производится запись данных
                  columns - список с названием заголовков
                  data - словарь с данными по людям
    '''

    with open(file_name, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for key in data:
            row = key.split(' ')
            row.extend(data[key])
            writer.writerow(row)


if __name__ == "__main__":

    # Чтение данных из файла, формирование списка заголовков, списка с данными по людям
    columns, data = read_file_csv("phonebook_raw.csv")

    # Приведение данных к требуемому формату
    data = create_adress_book(data)

    # Запись данных в требуемом формате в файл
    write_file_csv("result.csv", columns, data)

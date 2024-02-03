# Домашнее задание к лекции 2.2 «Regular expressions»

## Архитектура программы

Основной модуль "main" содержит следующие функции:

1. read_file_csv - функция считывает данные из файла с расширением .csv, формирует необходимые данные для дальнейшей работы;
2. create_number - функция приводит номер телефона к требуемому формату с использованием модуля re;
3. create_adress_book - функция объединяет данные по каждому человеку из разных записей, приводит данные к требуемому формату;
4. write_file_cs - функция выводит данные в файл

## Входные/выходные данные

1. Считывание данных производится из файла  "phonebook_raw.csv";
2. Вывод данных производится в файл "result.csv"
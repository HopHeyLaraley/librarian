import json
import random

class Book:
    """
    Класс, представляющий книгу в библиотеке.

    Атрибуты:
        __id (int): Идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (bool): Статус книги (True - в наличии, False - выдана).

    Методы:
        __init__: Инициализация новой книги с вводом данных от пользователя.
        set_id: Сеттер для записи ID из класса Библиотекарь.
        to_dict: Преобразует объект книги в словарь для хранения.
    """

    def __init__(self):
        self.__id = None
        self.title = input("Write title : ")
        self.author = input("Write author : ")
        self.year = int(input("Write year : "))
        self.status = True

    def set_id(self, id):
        self.__id = id

    def to_dict(self):
        return {
            'id': self.__id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }


class Librarian:
    """
    Класс для управления библиотекой.

    Атрибуты:
        __filename (str): Имя файла для хранения данных книг.
        __book_list (List[Dict]): Список книг, загруженных из файла.

    Методы:
        __init__: Инициализирует объект класса с загрузкой данных из файла.
        __load_books: Загружает список книг из файла JSON.
        __save_books: Сохраняет текущий список книг в файл JSON.
        show_books: Выводит список всех книг.
        __show_one_book: Выводит информацию об одной книге.
        set_book: Добавляет новую книгу в список и сохраняет изменения.
        __generate_id: Генерирует уникальный идентификатор для книги.
        remove_book: Удаляет книгу из списка по идентификатору.
        update_book: Изменяет статус книги по идентификатору.
        find_book: Поиск книги по названию, автору или году.
    """
    def __init__(self, filename = 'books.json'):
        self.__filename = filename
        self.__book_list = self.__load_books()

    def __load_books(self):
        try:
            with open(self.__filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def __save_books(self):
        with open(self.__filename, 'w') as file:
            json.dump(self.__book_list, file)

    def show_books(self):
        if not self.__book_list:
            print("No books available")
            return
        for book in self.__book_list:
            self.__show_one_book(book)

    def __show_one_book(self, book):
        print()
        print(f"ID : {book['id']}")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Year : {book['year']}")
        print(f"Status : {'В наличии' if book['status'] else 'Выдан'}")

    def find_book(self):
        field = int(input("Choose field :\n1.Title\n2.Author\n3.Year\n"))
        fields = ['title', 'author', 'year']
        if field in [1,2,3]:
            value = input("Write search value : ")
            for book in self.__book_list:
                if str(book[fields[field-1]]).lower() == str(value).lower():
                    print("Founded book : ")
                    self.__show_one_book(book)
                    return
        self.find_book()

    def set_book(self, book):
        id = self.__generate_id()
        book.set_id(id)
        self.__book_list.append(book.to_dict())
        self.__save_books()

    def __generate_id(self):
        existing_ids = []
        for book in self.__book_list:
            existing_ids.append(book['id'])
        while True:
            id = random.randint(0, 1000000)
            if id not in existing_ids:
                return id

    def remove_book(self, id):
        temp_book_list = []
        for book in self.__book_list:
            if id != book['id']:
                temp_book_list.append(book)
        if len(temp_book_list) < len(self.__book_list):
            self.__book_list = temp_book_list
            self.__save_books()
        else:
            print("ID not found")

    def update_book(self, id):
        for book in self.__book_list:
            if id == book['id']:
                change_or_not = ""
                while change_or_not.lower() not in ['y', 'n']:
                    change_or_not = input(f"Current status : {'В наличии' if book['status'] else 'Выдан'}. Change? (y/n)")
                    if change_or_not.lower() == 'y':
                        book['status'] = not book['status']
                        self.__save_books()
                        return
                    elif change_or_not.lower() == 'n':
                        return
        print("ID not found")
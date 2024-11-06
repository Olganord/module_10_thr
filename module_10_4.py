import random
import time
from threading import Thread
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом, по умолчанию None


class Guest(Thread):  # Создаем экземпляр потока "гости"
    def __init__(self, name):
        super().__init__()  # Позволяет получить доступ к методам базового класса Thread (поток)
        self.name = name

    def run(self):  # Метод выполняется при запуске потока "гости", представляет действия,
                    # которые должны быть выполнены в потоке.
        time.sleep(random.randint(3, 10))  # Ожидание от 3 до 10 секунд
        print(f"{self.name} покушал(-а) и ушёл(ушла)")  # Добавляем вывод сообщения после завершения "поедания"


class Cafe:
    def __init__(self, *tables_):
        self.queue = Queue()
        self.tables = tables_

    def guest_arrival(self, *guests_):  # гостевой приход
        for guest in guests_:
            assigned = False
            for table in self.tables:
                if table.guest is None:  # Проверка на свободный стол
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()  # Запуск потока для гостя
                    assigned = True
                    break

            if not assigned:  # Если нет свободных столов
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def manage_guests(self):  # Изменили название метода для большей ясности
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Проверяем, закончил ли гость
                    print(f"Стол номер {table.number} свободен")  # Сначала освобождаем стол
                    table.guest = None

                    # Если очередь не пуста, садим следующего
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        next_guest.start()  # Запуск потока для следующего гостя

            time.sleep(0.5)  # Небольшая пауза между итерациями цикла для предотвращения слишком частых проверок


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.manage_guests()

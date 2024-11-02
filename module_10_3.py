import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"\rПополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            request = random.randint(50, 500)
            print(f"\rЗапрос на {request}")
            with self.lock:
                if request > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                else:
                    self.balance -= request
                    print(f"Снятие: {request}. Баланс: {self.balance}")
            time.sleep(0.001)


# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')

import time
import random
from threading import Thread, Lock

class Bank:
    def __init__(self, balance=random.randint(50, 500)):
        self.balance = balance
        self.lock = Lock()
    def deposit(self):
        for x in range(100):
            y = random.randint(50, 500)
            self.balance += y
            time.sleep(0.1)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f'Пополнение:{y}. Баланс: {self.balance}')
    def take(self):
        for x in range(100):
            y = random.randint(50, 500)
            print(f'\nЗапрос на {y}')
            if y <= self.balance:
                self.balance -= y
                print(f'Снятие: {y}. Баланс: {self.balance}')
                time.sleep(0.01)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




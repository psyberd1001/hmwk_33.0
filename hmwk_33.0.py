import threading
import time
import random

class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()


    def deposit(self, tranzak=100):
        for i in range(tranzak):
            number = random.randint(50, 500)
            self.balance = self.balance + number
            print(f'Пополнение № {i}: {number}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.acquire():
                self.lock.release()
                time.sleep(0.001)

    def take(self, tranzak=100):
        for i in range(tranzak):
            number1 = random.randint(50, 500)
            print(f'Запрос № {i} на {number1}')
            if number1 <= self.balance:
                self.balance = self.balance - number1
                print(f'Снятие: {number1}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)



bank1 = Bank(600)
th1 = threading.Thread(target=Bank.deposit, args=(bank1,))
th2 = threading.Thread(target=Bank.take, args=(bank1,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank1.balance}')
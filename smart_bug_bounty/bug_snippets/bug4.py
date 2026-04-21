import threading
import time

balance = 100

def withdraw(amount):
    global balance
    # Intended: Deduct amount safely from balance.
    # BUG: Race condition due to non-atomic update.
    if balance >= amount:
        current = balance
        time.sleep(0.1) # Simulating context switch
        balance = current - amount
        print(f"Withdrawn: {amount}, New Balance: {balance}")

t1 = threading.Thread(target=withdraw, args=(70,))
t2 = threading.Thread(target=withdraw, args=(70,))
t1.start(); t2.start()
t1.join(); t2.join()

import threading
import time

balance = 100
lock = threading.Lock()

def withdraw(amount):
    global balance
    # FIX: Using Lock to ensure thread safety
    with lock:
        if balance >= amount:
            current = balance
            time.sleep(0.1) 
            balance = current - amount
            print(f"Success: New Balance: {balance}")
        else:
            print("Insufficient funds")

t1 = threading.Thread(target=withdraw, args=(70,))
t2 = threading.Thread(target=withdraw, args=(70,))
t1.start(); t2.start()
t1.join(); t2.join()

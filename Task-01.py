import queue
import time

#Створити чергу заявок
queue = queue.Queue()

def generate_request(Box):
    queue.put(Box)
    print("Added {} ".format(Box))
    

def process_request():
    if not queue.empty():
        print(queue.get())
        time.sleep(2)
    else:
        print("черга пуста")
i = 0
try:
    while True:
        #Поки користувач не вийде з програми:
        generate_request(i) 
        process_request()
        i += 1
except KeyboardInterrupt:
    print("Exit") 
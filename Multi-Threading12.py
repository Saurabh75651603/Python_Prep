from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)
            
            
class Hii(Thread):
    def run(self):
        for i in range(10):
            print('Hii')
            sleep(1)
        
        
t1 = Hello()
t2 = Hii()

t1.start()
sleep(1)
t2.start()


t1.join()
t2.join()
print("Bye")

# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(i)

# def print_letters():
#     for letter in 'ABCDE':
#         time.sleep(1)
#         print(letter)

# # Create two threads
# thread_numbers = threading.Thread(target=print_numbers)
# thread_letters = threading.Thread(target=print_letters)

# # Start the threads
# thread_numbers.start()
# thread_letters.start()

# # Wait for both threads to finish
# thread_numbers.join()
# thread_letters.join()

# print("Both threads have finished.")



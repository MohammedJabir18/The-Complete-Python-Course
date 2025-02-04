import threading
from time import sleep
import datetime as dt

print(threading.current_thread().name)


class Person:
    def __init__(self, user: list):
        self.user = user

    def hi_users(self):
        for i in self.user:
            print(f'hi, {i}')
            sleep(1)

    def hello_users(self):
        for i in self.user:
            print(f'hello, {i}')
            sleep(1)


if __name__ == "__main__":
    users = ['ajmal', 'arun', 'jabir', 'musthaq', 'arafath']
    start = dt.datetime.now()
    p1 = Person(users)

    thread_1 = threading.Thread(target=p1.hi_users)
    thread_2 = threading.Thread(target=p1.hello_users)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    # p1.hi_users()
    # p1.hello_users()
    end = dt.datetime.now()

    execution_time = end - start
    # Here divmod(a, b) function is used for 'a' is quotient and 'b' is reminder.
    hours, reminder = divmod(execution_time.total_seconds(), 36000)
    minutes, seconds = divmod(reminder, 60)
    total_time = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    print(f"Execution Time : {total_time}")

from time import sleep
import datetime
import multiprocessing


class Users:
    @staticmethod
    def hi_user(users: list):
        for i in users:
            print(f"Hi, {i}")
            sleep(1)

    @staticmethod
    def hello_user(users: list):
        for i in users:
            print(f"Hello, {i}")
            sleep(1)


if __name__ == "__main__":
    user = ["rahul", "musthafa", "hijas", "nabeel", "ramis"]
    start = datetime.datetime.now()
    user1 = Users()

    process1 = multiprocessing.Process(target=user1.hi_user, args=(user,))
    process2 = multiprocessing.Process(target=user1.hello_user, args=(user,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end = datetime.datetime.now()
    total_time = end - start

    hours, reminder = divmod(total_time.total_seconds(), 3600)
    minutes, seconds = divmod(reminder, 60)
    execution_time = f"{int(hours):02d}:{int(minutes):02d}:{float(seconds):.2f}"

    print(execution_time)

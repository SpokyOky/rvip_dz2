import random
import time
from threading import Thread


class Fork:
    is_using = False


class Philosopher:
    _isHunger = False
    _philosopherName = ""
    _number = -1
    _time = 0

    def __init__(self, name, number):
        self._philosopherName = name
        self._number = number

    def get_fork(self, fork):
        self._time = random.randint(0, 500000)
        print("Философ " + str(self._philosopherName) + " ожидает вилку (" + str(self._time) + " мс)\n")

        first = self._number
        second = (self._number + 1) % (len(fork) - 1)

        if fork[first].is_using and fork[second].is_using:
            return

        fork[first].is_using = True
        fork[second].is_using = True

        print("Философ " + str(self._philosopherName) + " кушает (" + str(self._time) + " мс)\n");
        print("Вилки " + str(first + 1) + " и " + str(second + 1) + " заняты (" + str(self._time) + " мс)\n");
        time.sleep(self._time)
        fork[first].is_using = False
        fork[second].is_using = False

    def start(self, fork):
        while True:
            time.sleep(self._time)
            self.change_status()
            if self._isHunger:
                self.get_fork(fork)

    def change_status(self):
        self._isHunger = not self._isHunger
        if not self._isHunger:
            print("Философ " + str(self._philosopherName) + " размышляет. (" + str(self._time) + " мс)\n")


countPh = int(input())
philosophers = []
forks = []
for i in range(0, countPh):
    forks.append(Fork)
    philosophers.append(Philosopher(str(i), i))
Thread(target=philosophers[i].start(forks))

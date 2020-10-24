#!/usr/bin/env python3
import time
import threading

class Chronometer:

    def __init__(self):
        self.clear()

    def init(self):
        self.clear()
        self.__stoped = False

        timing = threading.Thread(target=self.__init, daemon=True)
        timing.start()

    def clear(self):
        self.s = 0
        self.m = 0
        self.h = 0

    def stop(self):
        self.__stoped = True

    def __init(self):
        while not self.__stoped:
            time.sleep(1)
            self.s+=1
            if self.s == 59:
                self.m+=1
                self.s=-1
            elif self.m == 59:
                self.h+=1
                self.m=-1

    @property
    def time(self):
        return "{:02d}:{:02d}:{:02d}".format(self.h, self.m, self.s)


if __name__ == "__main__":
    # Testing...

    chrono = Chronometer()
    chrono.init()
    for _ in range(4):
        time.sleep(1)
        print(chrono.time)
    
    print("Stop")
    chrono.stop()
    print(chrono.time)
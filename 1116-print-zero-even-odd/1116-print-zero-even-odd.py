from threading import Barrier, Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.barriers = [Barrier(2),Barrier(2)]
        self.zero_lock = Lock()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            self.ct += 1
            self.barriers[self.ct % 2].wait()
        
    def even(self, printNumber):
        for _ in range(self.n//2):
            self.barriers[0].wait()
            printNumber(self.ct)
            self.zero_lock.release()
        
    def odd(self, printNumber):
        for _ in range((self.n+1)//2):
            self.barriers[1].wait()
            printNumber(self.ct)
            self.zero_lock.release()
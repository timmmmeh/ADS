import heapq
import random

class BuySell:
    def __init__(self):
        self.buy = []
        self.sell = []
        self.gen_rand()
        self.create_heap()
        self.work()

    def gen_rand(self):
        for i in range(10):
            self.buy.append(random.randint(0, 100))
            self.sell.append(random.randint(0, 100))
        print("Random Numbers")
        self.print_heap()

    def create_heap(self):
        heapq.heapify(self.buy)
        heapq.heapify(self.sell)
        print("Heapify")
        self.print_heap()

    def print_heap(self):
        print("buy: ", self.buy)
        print("sell: ", self.sell)
        print("")

    def work(self):
        print("Working")
        for i in range(len(self.buy)):
            self.print_heap()
            if self.buy[0] < self.sell[0]:
                heapq.heappop(self.buy)
            else:
                heapq.heappop(self.buy)
                heapq.heappop(self.sell)

if __name__ == '__main__':
    BuySell()

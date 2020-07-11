import time


class TimeWatch:
    time_dict = {}

    def start_measuring(self):
        self.start = time.time()

    def stop_measuring(self, name='operation'):
        self.end = time.time()
        print(f'\nElapsed time for {name}: {self.end - self.start}')

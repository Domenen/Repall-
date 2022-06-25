import time

class Timing:
    def __init__(self, func):
        self.stage = 100
        self.func = func

    def __call__(self, *args, **kwargs):
        mid_time = 0 
        for _ in range(self.stage):
            t1 = time.time()
            self.func(*args, **kwargs)
            t2 = time.time()
            mid_time += (t2 - t1)
        mid_time /= self.stage
        fn = self.func.__name__
        print("Функция: %s \nКол-во запусков: %s \nСреднее время: %.5f секунд" % (fn, self.stage, mid_time))

        return self.func(*args, **kwargs)

@Timing
def foo(func):
    for _ in range(func):
        pass

foo(10000000)



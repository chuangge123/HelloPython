import time as t
class MyTimer():
    def __init__(self):
        self.prompt="未开始定时"
        self.lasted=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt
    __repr__=__str__
    def start(self):
        self.end=t.localtime()
        print("计时开始")
    def stop(self):
        self.end=t.localtime()
        self._calc()
        print("计时结束")
    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            self.prompt+=str(self.lasted[index])
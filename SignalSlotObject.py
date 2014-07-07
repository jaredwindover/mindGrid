

class SignalSlotObject:
    def __init__(self):
        self.functions = []

    def connect(self,f):
        self.functions.append(f)
        
    def emit(self,*args):
        for f in self.functions:
            f(*args)

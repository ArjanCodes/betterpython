class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating Logger")
    
    def log(self, msg):
        print(msg)

class CustomLogger(Logger):
    def __init__(self):
        print("Creating Custom logger")
        super().__init__()

logger = CustomLogger()
logger2 = CustomLogger()
print(logger)
print(logger2)
logger.log("Hello")
logger2.log("Helloooo")
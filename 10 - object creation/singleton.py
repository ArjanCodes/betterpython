class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    def __init__(self):
        print("Creating Logger")
    
    def log(self, msg):
        print(msg)

logger = Logger()
logger2 = Logger()
print(logger)
print(logger2)
logger.log("Hello")
logger2.log("Helloooo")
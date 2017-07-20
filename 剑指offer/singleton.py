class Singleton:
    __singleton = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__singleton == None:
            cls.__singleton = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__singleton

    def getInstance(self):
        x  = Singleton()
        return x



s1 = Singleton()
s2 = Singleton()
s3 = Singleton.getInstance()
print(id(s1), id(s2), id(s3))

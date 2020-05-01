from .animal import Animal

class Dog(Animal):
    def __init__(self):
        pass

# Not recomended
# For this it is important that in sounds folder, __init__.py defines __all__ list with the modules to import
from sounds import *
beep.d()

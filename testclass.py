# testing to confirm how to use and properly create classes
# will be used to create classes for motors, cameras, and other peripherals

class aux:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def modify_all(self):
        self.a *=2
        self.b *=3
        self.c *=4

    def print_all(self):
        print("a = "+str(self.a)+"\nb = "+str(self.b)+"\nc = "+str(self.c))



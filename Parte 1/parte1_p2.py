class way:
    def simpson(self) -> (str, int):
        pass
    def trapecio(self) -> (str, int):
        pass
    def boole(self) -> (str, int):
        pass

class simple(way):
    def simpson(self) -> (str, int):
        return '',0
    def trapecio(self) -> (str, int):
        return '',0
    def boole(self) -> (str, int):
        return '',0

class compuesto(way):
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    def simpson(self) -> (str, int):
        return '',0
    def trapecio(self) -> (str, int):
        return '',0
    def boole(self) -> (str, int):
        return '',0

value: way = simple()
print (value.simpson())
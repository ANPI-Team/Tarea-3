class way:
    def simpson(self, func, a, b) -> (str, float):
        pass
    def trapecio(self, func, a, b) -> (str, float):
        pass
    def boole(self, func, a, b) -> (str, float):
        pass

class simple(way):
    def simpson(self, func, a, b) -> (str, float):
        return func,0.0
    def trapecio(self, func, a, b) -> (str, float):
        return func,0.0
    def boole(self, func, a, b) -> (str, float):
        return func,0.0

class compuesto(way):
    def simpson(self, func, a, b) -> (str, float):
        return func,0.0
    def trapecio(self, func, a, b) -> (str, float):
        return func,0.0
    def boole(self, func, a, b) -> (str, float):
        return func,0.0


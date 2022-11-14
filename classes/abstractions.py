class AbstractClass:
    def __init__(self, value):
        self.value = value
    def do_something(self):
        raise NotImplementedError("Subclass must implement abstract method")
class DoAdd42(AbstractClass):
    def do_something(self):
        return self.value + 42
class DoMul42(AbstractClass):
    def do_something(self):
        return self.value * 42

x = DoAdd42(10)
y = DoMul42(10)
z = AbstractClass(10)
print(x.do_something())
print(y.do_something())
print(z.do_something())
# Output:

# 52
# 420
# Traceback (most recent call last):

# @property と @<name>.setter デコレーターを使う方法
class Foo:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("getter")
        return self._value

    @value.setter
    def value(self, value):
        print("setter")
        self._value = value


# property 関数を使う方法
class Bar:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        print("getter")
        return self._value

    def set_value(self, value):
        print("setter")
        self._value = value

    value = property(get_value, set_value)


foo = Foo(10)

print(foo.value)

foo.value = 20
print(foo.value)

bar = Bar(100)

print(bar.value)

bar.value = 200
print(bar.value)

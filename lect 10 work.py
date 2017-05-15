
class Table:
    pass
print(type(Table))
table = Table()
table.l = 150
table.w = 60
table.h = 70
table.color = "red"
print(vars(table))

# ==========================

class Table:
    def f(self):
        print(self)
        self.x =1

table = Table()
print(table)
print(table.f())
print(vars(table))

t= Table()
print(vars(t))

# ==========================

class Table:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def get_volume(self):
        return self.h*self.w*self.l
table = Table(150, 60, 70)
print(table.get_volume())

# ==========================

class A:
    def __init__(self):
        self.a = 0
        self._donttouchme = 0
        self.__secret = 0

a=A()
print(a.a)
print(a._donttouchme)
print(vars(a))
print(a._A__secret)

# ==========================

print(dir(object))

# ==========================

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return  "Shape({}, {})".format(self.x, self.y)

s = Shape(2,3)
print(vars(s))
print(s)

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r =r
        self.center = Point(x, y)
    def __repr__(self):
        return  "Shape({}, {}, {})".format(self.x, self.y, self.r)

c = Circle(5,6,8)
print(c)

# ==============================

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def say(self):
        print('Myaw!')
    def move(self):
        print('Run')

class Frog(Animal):
    def say(self):
        print('Quack!')
    def move(self):
        print('Jump')

class Snake(Animal):
    def say(self):
        print('Shhhhh!')
    def move(self):
        print('Crawl')

zoo = [Cat('Tom'), Cat('Barsik'), Frog('Kermit'), Snake('Kaa')]

for animal in zoo:
    print(animal.say())
    print(animal.move())

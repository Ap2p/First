class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Ap2p')
p.sayHi()
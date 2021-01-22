from Animal import Animal


class Cat(Animal):
    def __init__(self):
        super().__init__()
        hair = 'shorthair'

    def catchmouse(self):
        print('Cat can catch Mouse')

    def woo(self):
        print('miao~miao')


if __name__ == '__main__':
    hellokitt = Cat()
    hellokitt.run()
    hellokitt.catchmouse()
    hellokitt.woo()

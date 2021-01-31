class Animal:
    def __init__(self):
        self.name = 'Kitt'
        self.color = 'Pink'
        self.age = 3
        self.gender = 'female'
        print(f'Animal get '
              f'{self.name} '
              f'{self.color} '
              f'{self.age} '
              f'{self.gender}')

    def woo(self):
        print('Animal can whoop')

    def run(self):
        print('Animal can run')


class Apple():
    def __init__(self, apple_color):
        self. apple_color = apple_color

    def __str__(self):
        return 'this is %s apple' % self.apple_color


apple1 = Apple('red')
apple2 = Apple('green')


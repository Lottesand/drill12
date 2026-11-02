from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.x = 400
        self.y = 30
        self.image.draw(self.x, self.y)

    def update(self):
        pass

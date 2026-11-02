from pico2d import load_image
import game_world


class Grass1:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.x = 400
        self.y = 30
        self.image.draw(self.x, self.y)

    def update(self):
        pass

class Grass2:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.x = 400
        self.y = 10
        self.image.draw(self.x, self.y)

    def update(self):
        pass

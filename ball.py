from pico2d import load_image
import game_world


class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y
        self.velocity = velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        # 화면 밖으로 완전히 벗어나면 게임 월드에서 스스로 제거
        if self.x < -25 or self.x > 800 + 25:
            game_world.remove_object(self)

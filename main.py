import os
from pico2d import *

# 작업 디렉터리를 스크립트 위치로 설정하여 리소스 로드 보장
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from boy import Boy
from grass import Grass1
from grass import Grass2
import game_world


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global boy

    grass = Grass2()
    game_world.add_object(grass, 2)

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass1()
    game_world.add_object(grass, 0)



def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True

open_canvas()
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()

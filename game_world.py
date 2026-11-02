# 게임월드 리스트 초기화
# world = []  # 객체들의 리스트 (단일 리스트 및 레이어 리스트 모두 호환)

world = [ [], []] # 객체들의 리스트, 빈 리스트

def add_object(o, depth=0):
    global world
    if world and isinstance(world[0], list):
        world[depth].append(o)
    else:
        world.append(o)


def add_objects(ol, depth=0):
    global world
    if world and isinstance(world[0], list):
        world[depth] += ol
    else:
        world += ol


def remove_object(o):
    global world
    if world and isinstance(world[0], list):
        for layer in world:     # 모든 레이어들 순회하면서 레이어 제거
            if o in layer:      # 객체가 해당 레이어 존재하면 제거
                layer.remove(o)
                return      # 제거 후 함수 종료
    else:
        if o in world:
            world.remove(o)
            return


# 게임 로직 (업데이트 중 객체가 스스로 삭제되어도 안전하도록 복사본 순회)
def update():
    if world and isinstance(world[0], list):
        for layer in world:
            for o in layer.copy():
                o.update()
    else:
        for o in world.copy():
            o.update()


# 게임 월드 렌더링
def render():
    if world and isinstance(world[0], list):
        for layer in world:
            for o in layer:
                o.draw()
    else:
        for o in world:
            o.draw()

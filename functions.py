import curses
import random
import time


def select_difficulty():
    difficulty = {
        '1': 1000,
        '2': 500,
        '3': 150,
        '4': 90,
        '5': 35,
        '6': 10
    }
    while True:
        answer = input('Selecione a dificuldade (1 - De boa / 6 - DOOM SPEED): ')
        game_speed = difficulty.get(answer)
        if game_speed is not None:
            return game_speed
        print('Escolha a dificuldade de 1 a 6 \n')


def draw_screen(window):
    window.clear()
    window.border(0)


def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height - 2), random.randint(1, width - 2)]


def snake_hit_fruit(snake, fruit):
    return fruit in snake


def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)


def get_new_directions(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction

    return None


def draw_snake(snake, window):
    head = snake[0]
    draw_actor(head, window, char="@")
    body = snake[1:]
    for body_part in body:
        draw_actor(body_part, window, char=":")


def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_RIGHT:
            actor[1] += 1


def move_snake(snake, direction, snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    if not snake_ate_fruit:
        snake.pop()


def snake_hit_border(snake, window):
    head = snake[0]
    return check_crash(head, window)


def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body


def finish_game(score, window):
    height, width = window.getmaxyx()
    s = f'Você perdeu. Sua pontuação: {score}'
    y = int(height / 2)
    x = int((width - len(s)) / 2)
    window.addstr(y, x, s)
    window.refresh()
    time.sleep(5)


def direction_is_opposite(direction, current_direction):
    match direction:
        case curses.KEY_UP:
            return current_direction == curses.KEY_DOWN
        case curses.KEY_DOWN:
            return current_direction == curses.KEY_UP
        case curses.KEY_LEFT:
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_RIGHT:
            return current_direction == curses.KEY_LEFT


def check_crash(actor, window):
    height, width = window.getmaxyx()
    if actor[0] <= 0 or actor[0] >= height - 1:
        return True
    if actor[1] <= 0 or actor[1] >= width - 1:
        return True

    return False

from functions import *

def game_loop(window, game_speed):
    snake = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15]
    ]
    current_direction = curses.KEY_DOWN
    snake_ate_fruit = False
    fruit = get_new_fruit(window)
    points = 0

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char=curses.ACS_DIAMOND)

        directions = get_new_directions(window=window, timeout=game_speed)

        if directions is None:
            directions = current_direction
        if direction_is_opposite(directions, current_direction):
            directions = current_direction

        move_snake(snake=snake, direction=directions, snake_ate_fruit=snake_ate_fruit)
        if snake_hit_border(snake=snake, window=window):
            break
        if snake_hit_itself(snake):
            break
        if snake_hit_fruit(snake, fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window)
            points += 1
        else:
            snake_ate_fruit = False

        current_direction = directions

    finish_game(points, window)

if __name__ == '__main__':
    curses.wrapper(game_loop, game_speed=select_difficulty())
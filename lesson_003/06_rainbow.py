# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# step = 0
# for color in rainbow_colors:
#     start_point = sd.get_point(50 + step, 50)
#     end_point = sd.get_point(350 + step, 450)
#     sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
#     step += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# circle(center_position, radius=50, color=COLOR_YELLOW, width=1):
step = 0
radius = 500
for color in rainbow_colors:
    center_position = sd.get_point(700, -100)
    sd.circle(center_position=center_position, radius=radius + step, color=color, width=40)
    step += 40

sd.pause()

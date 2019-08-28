import time

display = [[0] * 80 for rows in range(30)]


def point_to_point(points: tuple = ([5, 10], [5, 50]), tail: int = 1, delay: float = 0.05):
    points = list(points)
    point_from = ()
    dot = []
    dot_queue = []

    for cords in points:
        if len(point_from) == 0:
            point_from = cords
            dot = list(point_from)
            continue

        # choose in what direction move
        if point_from[0] != cords[0]:
            if point_from[0] > cords[0]:
                # move up
                while dot != cords:
                    display[dot[0]][dot[1]] = 1
                    draw(delay * 1.66)
                    dot_queue.append(list(dot))
                    if len(dot_queue) == tail:
                        dot_to_delete = dot_queue.pop(0)
                        display[dot_to_delete[0]][dot_to_delete[1]] = 0
                    dot[0] -= 1

            elif point_from[0] < cords[0]:
                # move down
                while dot != cords:
                    display[dot[0]][dot[1]] = 1
                    draw(delay * 1.66)
                    dot_queue.append(list(dot))
                    if len(dot_queue) == tail:
                        dot_to_delete = dot_queue.pop(0)
                        display[dot_to_delete[0]][dot_to_delete[1]] = 0
                    dot[0] += 1

        else:
            if point_from[1] > cords[1]:
                # move left
                while dot != cords:
                    display[dot[0]][dot[1]] = 1
                    draw(delay)
                    dot_queue.append(list(dot))
                    if len(dot_queue) == tail:
                        dot_to_delete = dot_queue.pop(0)
                        display[dot_to_delete[0]][dot_to_delete[1]] = 0
                    dot[1] -= 1

            elif point_from[1] < cords[1]:
                # move right
                while dot != cords:
                    display[dot[0]][dot[1]] = 1
                    draw(delay)
                    dot_queue.append(list(dot))
                    if len(dot_queue) == tail:
                        dot_to_delete = dot_queue.pop(0)
                        display[dot_to_delete[0]][dot_to_delete[1]] = 0
                    dot[1] += 1

        # set new start point
        point_from = cords
        dot = point_from


def draw(freq: float = 0.05):
    to_print = ''

    time.sleep(freq)
    print('\n' * 4)

    for line in display:
        for item in line:
            to_print += '#' if item == 1 else '.'
        print(to_print)
        to_print = ''


def go_circle(lu: list, ld: list, rd: list, ru: list, tail: int = 1):
    dot = list(lu)
    dot_queue = []

    while dot != ld:
        dot[0] += 1
        display[dot[0]][dot[1]] = 1
        dot_queue.append(list(dot))
        draw(0.083)
        if len(dot_queue) == tail:
            dot_to_delete = dot_queue.pop(0)
            display[dot_to_delete[0]][dot_to_delete[1]] = 0

    while dot != rd:
        dot[1] += 1
        display[dot[0]][dot[1]] = 1
        dot_queue.append(list(dot))
        draw()
        if len(dot_queue) == tail:
            dot_to_delete = dot_queue.pop(0)
            display[dot_to_delete[0]][dot_to_delete[1]] = 0

    while dot != ru:
        dot[0] -= 1
        display[dot[0]][dot[1]] = 1
        dot_queue.append(list(dot))
        draw(0.083)
        if len(dot_queue) == tail:
            dot_to_delete = dot_queue.pop(0)
            display[dot_to_delete[0]][dot_to_delete[1]] = 0

    while dot != lu:
        dot[1] -= 1
        display[dot[0]][dot[1]] = 1
        dot_queue.append(list(dot))
        draw()
        if len(dot_queue) == tail:
            dot_to_delete = dot_queue.pop(0)
            display[dot_to_delete[0]][dot_to_delete[1]] = 0

    while len(dot_queue):
        dot_to_delete = dot_queue.pop(0)
        display[dot_to_delete[0]][dot_to_delete[1]] = 0
        draw()


pts = (
    [5, 10],
    [10, 10],
    [10, 20],
    [5, 20],
    [5, 3],
    [23, 3],
    [23, 55],
)

point_to_point(pts, 50)
# go_circle([13, 36], [17, 36], [17, 44], [13, 44], 10)

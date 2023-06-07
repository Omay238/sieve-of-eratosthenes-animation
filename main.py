import pygame as pg
import numpy

s = 15

max_value = s*s
max_sqrt = int(numpy.ceil(numpy.sqrt(max_value)))

size = 40

pg.init()
screen = pg.display.set_mode((max_sqrt * (size + 5) + 10, max_sqrt * (size + 5) + 10))
clock = pg.time.Clock()
running = True

pg.font.init()

font = pg.font.Font("./OpenSans-Regular.ttf", 20)

nums = []
for i in range(2, max_value + 1):
    nums.append(i)

to_remove = []

a = 2
n = 2

while running:
    pg.event.pump()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    screen.fill("black")

    # render
    for i in range(0, max_sqrt):
        for j in range(0, max_value // max_sqrt):
            if (1 + i + j * max_sqrt) in nums:
                if (1 + i + j * max_sqrt) == a and a <= max_sqrt:
                    pg.draw.rect(screen, "green",
                                 (int(size * 0.1) + i * int(size * 1.1), int(size * 0.1) + j * int(size * 1.1),
                                  size, size), border_radius=int(size * 0.1))
                elif (1 + i + j * max_sqrt) == nums[n] and a <= max_sqrt:
                    pg.draw.rect(screen, "yellow",
                                 (int(size * 0.1) + i * int(size * 1.1), int(size * 0.1) + j * int(size * 1.1),
                                  size, size), border_radius=int(size * 0.1))
                elif (1 + i + j * max_sqrt) in to_remove:
                    pg.draw.rect(screen, "red",
                                 (int(size * 0.1) + i * int(size * 1.1), int(size * 0.1) + j * int(size * 1.1),
                                  size, size), border_radius=int(size * 0.1))
                else:
                    pg.draw.rect(screen, "white",
                                 (int(size * 0.1) + i * int(size * 1.1), int(size * 0.1) + j * int(size * 1.1),
                                  size, size), border_radius=int(size * 0.1))
                f = font.render(str(1 + i + j * max_sqrt), True, "black")
                screen.blit(f, (int(size * 0.1) + i * int(size * 1.1), int(size * 0.1) + j * int(size * 1.1)))
    # end render

    # logic
    if a < max_sqrt:
        if nums[n] % a == 0 and nums[n] != a:
            to_remove.append(nums[n])
        if n == len(nums) - 1:
            nums = [i for i in nums if i not in to_remove]
            a = a + 1
            while a not in nums:
                a = a + 1
            n = a
            to_remove = []
        else:
            n = n + 1
    # end logic

    pg.display.flip()
    clock.tick(60)

pg.quit()

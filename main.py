import pygame as pg

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

pg.font.init()

font = pg.font.Font("./OpenSans-Regular.ttf", 40)

nums = []
for i in range(2, 101):
    nums.append(i)

to_remove = []

a = 2
n = 2

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("black")

    # render
    for i in range(0, 10):
        for j in range(0, 10):
            if (1 + i + j * 10) in nums:
                if (1 + i + j * 10) == a:
                    pg.draw.rect(screen, "green", (i * 55, j * 55, 50, 50))
                elif (1 + i + j * 10) == n:
                    pg.draw.rect(screen, "yellow", (i * 55, j * 55, 50, 50))
                else:
                    pg.draw.rect(screen, "red" if (1 + i + j * 10) in to_remove else "white", (i*55, j*55, 50, 50))
                f = font.render(str(1 + i + j * 10), True, "black")
                screen.blit(f, (i*55, j*55))
    # end render

    # logic
    if a < 10:
        if nums[n] % a == 0 and nums[n] != a:
            to_remove.append(nums[n])
        if n == len(nums) - 1:
            nums = [i for i in nums if i not in to_remove]
            n = a
            a = a + 1
        else:
            n = n + 1
    # end logic
    pg.display.flip()

    clock.tick(10)

pg.quit()

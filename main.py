from math import cos, sin, radians
import pygame

pygame.init()


class Ball:
    def __init__(self, x, y, vx, vy, coef_rebondissement, win_size_, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.coef_rebondissement = coef_rebondissement
        self.win_size = win_size_
        self.falling_time = 0
        self.gravity = 9.81
        self.color = color

    def impulse(self, vx, vy):
        self.vx += vx
        self.vy += vy


    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.falling_time += dt
        self.vy += self.gravity * self.falling_time
        if self.x < 0:
            self.x = 0
            self.vx *= -self.coef_rebondissement
        elif self.x > self.win_size[0]:
            self.x = self.win_size[0]
            self.vx *= -self.coef_rebondissement

        if self.y < 0 - 20:
            self.y = 0
            self.vy *= -self.coef_rebondissement
        elif self.y > self.win_size[1] - 10:
            self.y = self.win_size[1] - 10
            self.vy *= -self.coef_rebondissement

    def draw(self, window_):

        pygame.draw.circle(window_, self.color, (int(self.x), int(self.y)), 10)


def convert_angle_to_vx_vy(angle):
    vx = cos(radians(angle))
    vy = sin(radians(angle))
    return vx, vy


def create_all_colors(nb_colors):
    colors_ = []
    color_count = (256*3) / nb_colors
    for i in range(nb_colors):
        r = 0
        g = 0
        b = 0

        if color_count * i < 256:
            r = 255 - color_count * i
            g = color_count * i
        elif color_count * i < 512:
            c = color_count*i - 256
            g = 255 - c
            b = c
        else:
            c = color_count * i - 512
            b = 255 - c
            r = c

        colors_.append((r, g, b))

    return colors_
    

win_size = (1000, 1000)
window = pygame.display.set_mode(win_size)

# creates balls
balls = []
nb_balls = 50000
colors = create_all_colors(nb_balls)
for count in range(nb_balls):
    angle_count = 360 / nb_balls
    vx, vy = convert_angle_to_vx_vy(angle_count*count)
    vx *= 1000
    vy *= 1000

    print(vx, vy)

    ball = Ball(500, 500, vx, vy, 1, win_size, (colors[count][0], colors[count][1], colors[count][2]))
    balls.append(ball)

run = True
count = 0
while run:
    window.fill((0, 0, 0))

    for ball in balls:
        ball.move(0.01)
        ball.draw(window)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()

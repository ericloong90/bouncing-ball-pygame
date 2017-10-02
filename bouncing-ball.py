import sys, pygame
pygame.init()

size = width, height = 500, 400
x, y = 500, 400
moveX, moveY = 0, 0
speed = [moveX, moveY]
black = 0, 0, 0
grey = 246, 246, 246
FullScreen = False
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption('Bouncing ball')
ball = pygame.transform.scale(pygame.image.load('ball.png'), (70, 70))
gravityAcceleration = 0.3
horizontalAcceleration = 0
verticalSpeed = [0, 0]
horizontalSpeed = [0, 0]
ballrect = ball.get_rect()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                FullScreen = not FullScreen
                if FullScreen:
                    screen = pygame.display.set_mode(size, pygame.HWSURFACE|pygame.FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(size, 0, 32)


    keys = pygame.key.get_pressed()

    # Provide controls from keyboard, even when key is held down
    if keys[pygame.K_LEFT]:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = -10
    
    if keys[pygame.K_RIGHT]:
        horizontalSpeed[0] = 0
        horizontalSpeed[1] = 10

    if keys[pygame.K_UP]:
        verticalSpeed[0] = 0
        verticalSpeed[1] = -10

    verticalSpeed[0] = gravityAcceleration + verticalSpeed[1]
    y += verticalSpeed[0]
    verticalSpeed[1] = verticalSpeed[0]

    horizontalSpeed[0] = horizontalAcceleration + horizontalSpeed[1]
    x += horizontalSpeed[0]
    horizontalSpeed[1] = horizontalSpeed[0]

    if x < 0:
        x = 0
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if x > (width- ballrect.right):
        x = width- ballrect.right
        horizontalSpeed = [-horizontalSpeed[0] * 0.7, -horizontalSpeed[1] * 0.7]
    if y < 0:
        y = 0
        verticalSpeed = [0, 0]
    if y > (height - ballrect.bottom):
        y = height - ballrect.bottom
        verticalSpeed = [-verticalSpeed[0] * 0.7, -verticalSpeed[1] * 0.7]
        if (y == (height - ballrect.height)):
            horizontalSpeed = [horizontalSpeed[0] * 0.95, horizontalSpeed[1] * 0.95]

    
    clock.tick(60)
    screen.fill(grey)
    screen.blit(ball, (x, y))
    pygame.display.update()
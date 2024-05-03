# Pong made by Toby.M, 5/2/24

import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
running = True
dt = 0
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
p1_pos = pygame.Rect(screen.get_width() - screen.get_width() + 10,
                     screen.get_height() / 2 - 50, 10, 100)
p2_pos = pygame.Rect(screen.get_width() - 20,
                     screen.get_height() / 2 - 50, 10, 100)
ballXBool = False
ballYBool = False
p1_score = 0
p2_score = 0

def ballReset():
    ball_pos.x = screen.get_width() / 2
    ball_pos.y = screen.get_height() / 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    ball = pygame.draw.circle(screen, "white", ball_pos, 10)
    pygame.draw.rect(screen, "blue", p1_pos)
    pygame.draw.rect(screen, "red", p2_pos)

    p1Keys = pygame.key.get_pressed()
    if p1Keys[pygame.K_w]:
        if p1_pos.y > 0:
            p1_pos.y -= 300 * dt
    if p1Keys[pygame.K_s]:
        if p1_pos.y < 620:
            p1_pos.y += 300 * dt
    p2Keys = pygame.key.get_pressed()
    if p2Keys[pygame.K_UP]:
        if p2_pos.y > 0:
            p2_pos.y -= 300 * dt
    if p2Keys[pygame.K_DOWN]:
        if p2_pos.y < 620:
            p2_pos.y += 300 * dt

    if p1_pos.x - 10 <= ball_pos.x <= p1_pos.x + 20 and p1_pos.y <= ball_pos.y <= p1_pos.y + 100:
        ballXBool = True
    if p2_pos.x - 10 <= ball_pos.x <= p2_pos.x + 20 and p2_pos.y <= ball_pos.y <= p2_pos.y + 100:
        ballXBool = False

    def ballL():
        ball_pos.x += 300 * dt
    def ballR():
        ball_pos.x -= 300 * dt
    if ballXBool:
        ballL()
    if not ballXBool:
        ballR()

    if ball_pos.y < 10:
        ballYBool = True
    if ball_pos.y > 710:
        ballYBool = False
    def ballU():
        ball_pos.y += 300 * dt
    def ballD():
        ball_pos.y -= 300 * dt
    if ballYBool:
        ballU()
    if not ballYBool:
        ballD()

    resetKey = pygame.key.get_pressed()
    if ball_pos.x <= -200:
        p2_score += 1
        ballReset()

    if ball_pos.x >= 1480:
        p1_score += 1
        ballReset()
    
    font = pygame.font.Font(None, 36)
    text = font.render(str(p1_score) + ' : ' + str(p2_score), True, (255, 255, 255))
    screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, 20))

    #debug
    #print(p1_score, p2_score)
    #print(ballXBool, ball_pos.x)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()

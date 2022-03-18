import pygame
import random
import math
from pygame import mixer

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
bckg = pygame.image.load("backgroundw.png")

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# set display caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# create the player
playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (70, 50))
playerX = 370
playerY = 520
playerX_change = 0
playerY_change = 0

# accuracy, defeat sound, game over text control variables
accuracy = 0
end = 0
defeat_sound = 0

# lists for enemy settings and using a loop to set each enemy's properties
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_e = 5

for i in range(num_of_e):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (48, 48))
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(30, 250))
    enemyX_change.append(1.6)
    enemyY_change.append(50)

# creating the bullet
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet, (32, 32))
bulletX = 0
bulletY = 520
bulletX_change = 0
bulletY_change = 10
bullet_state = "Ready"

# score tracking variable and  font and size for the text
score_val = 0
font = pygame.font.Font("Neo Tech.ttf", 32)

# location of the score text
textX = 5
textY = 5

# game over font
font_l = pygame.font.Font("Neo Tech.ttf", 72)


# prints game over text
def game_over():
    last = font_l.render("Game Over", True, (255, 0, 0))
    screen.blit(last, (200, 180))


# shows score
def show_score(x, y, string):
    score = font.render(string + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))


# shows accuracy at the end of the game
def show_accuracy(x, y):
    if accuracy == 0:
        score = font.render("Accuracy: 0%", True, (255, 255, 255))
    else:
        score = font.render(f"Accuracy: {int(score_val / accuracy * 100)}%", True, (255, 255, 255))
    screen.blit(score, (x, y))


# draws the player
def player(x, y):
    screen.blit(playerImg, (x, y))


# draws enemies
def enemy(x, y, k):
    screen.blit(enemyImg[k], (x, y))


# fires the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet, (x + 16, y + 10))


# detects collision
def collision_det(e_X, e_Y, b_X, b_Y):
    distance = math.sqrt(math.pow(e_X - b_X, 2) + math.pow(e_Y - b_Y, 2))
    if distance < 30:
        return True
    else:
        return False


# Game loop
# anything you want to be continuous inside the game goes inside the loop
running = True
while running:
    screen.blit(bckg, (0, 0))  # fill the screen with that picture
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 'key down' means pressed while 'key up' means no longer pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                accuracy += 1
                if bullet_state == "Ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
    # setting boundaries for the sides
    playerX += playerX_change
    if playerX <= 0:
        playerX = 1
    elif playerX >= screen.get_width() - playerImg.get_width():
        playerX = screen.get_width() - playerImg.get_width()

    # setting boundaries for up and down
    playerY += playerY_change
    if playerY <= 0:
        playerY = 1
    elif playerY >= screen.get_height() - playerImg.get_height():
        playerY = screen.get_height() - playerImg.get_height()

    # enemy
    for i in range(num_of_e):
        if enemyY[i] > 440:

            for j in range(num_of_e):
                # moving every enemy that passes the line out of the screen and making each transparent
                enemyY[j] = 2000
                enemyImg[j].fill(0)
            # not sure if end is correct
            if defeat_sound == 0:
                over = mixer.Sound("defeat.mp3")
                over.play()
                defeat_sound = 1
            end = 1
            game_over()
            break
        # adjusting the position of the enemies
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1.6
            enemyY[i] += enemyX_change[i]
        elif enemyX[i] >= screen.get_width() - enemyImg[i].get_width():
            enemyX_change[i] = -1.6
            enemyY[i] += enemyY_change[i]

        collision = collision_det(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("break.wav")
            explosion_sound.play()
            bulletY = playerY
            bullet_state = "Ready"
            score_val += 1
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(50, 200)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "Ready"
    if bullet_state == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    # the text that pops up when the game is over
    if end == 0:
        show_score(textX, textY, "Score: ")
    else:
        show_score(280, 120, "Final Score: ")
        show_accuracy(280, 70)

    player(playerX, playerY)
    pygame.display.update()

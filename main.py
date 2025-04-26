import random
import pgzrun

WIDTH = 1200
HEIGHT = 600
TILE = "GALAGA GAME"

is_game_over = False
score = 0
lives = 3
speed = 5

#Create a Galaga
galaga = Actor("galaga")
galaga.pos = (600,540)

enemies = []
bullets = []

#Creating the enemies
for i in range(8):
    enemy = Actor("enemy")
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

def display_score():
    screen.draw.text(f"Score: {score}", (50,30))
    screen.draw.text(f"Lives: {lives}", (50,60))

#Creating bullets
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = galaga.x
        bullet.y = galaga.y - 50
        bullets.append(bullet)

#Update the game
def update():
    global lives,score
    #move te ship left or right
    if keyboard.left:
        galaga.x -= speed
        if galaga.x <= 0:
            galaga.x = 0
    elif keyboard.right:
        galaga.x += speed
        if galaga.x >= WIDTH:
            galaga.x = WIDTH

    #Make bullets move
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10



pgzrun.go()
    
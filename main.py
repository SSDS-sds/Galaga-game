import random
import pgzrun

WIDTH = 1200
HEIGHT = 600
TITLE = "GALAGA GAME"

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

    #Move enemies
    for enemy in enemies:
        enemy.y += 5
    
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
            
        #Check for collision of bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score = score + 100
                enemies.remove(enemy)
                bullets.remove(bullet)
        
        #Check for collision with Galaga
        if enemy.colliderect(galaga):
            lives = lives - 1
            enemies.remove(enemy)
            if lives == 0:
                game_over()

    #Continueously create new enemies
    if len(enemies) < 8:
        enemy = Actor("enemy")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

#Function to draw gamestate
def draw():
    if lives > 0:
        screen.clear()
        screen.fill("red")
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        galaga.draw()
        display_score()
    else:
        game_over_screen()

def game_over():
    is_game_over = True

def game_over_screen():
    screen.clear()
    screen.fill("sky blue")
    screen.draw.text("GAME OVER!!!", (WIDTH/2, HEIGHT/2), fontsize = 50, color = "black")
    screen.draw.text(f"Your final score was {score}", (WIDTH/2, HEIGHT/2 + 50), fontsize = 40, color = "black")
    screen.draw.text("Press SPACE to play again", (WIDTH/2, HEIGHT/2 + 100), fontsize = 45, color = "black")

    if keyboard.SPACE:
        restart_game()

def restart_game():
    global score, lives, bullets, enemies
    score = 0
    lives = 3
    bullets = []
    enemies = []



    for enemy in enemies:
        enemy = Actor("enemy")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

pgzrun.go()
    
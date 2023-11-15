import pygame as pg
import os
import random
pg.init()
WIDTH = 1280
HEIGHT = 720
screen = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
map_image = pg.image.load(os.path.join('assets', 'map.png'))
head_image = pg.image.load(os.path.join('assets', 'head.png'))
body_image = pg.image.load(os.path.join('assets', 'body.png'))
food_image =  pg.image.load(os.path.join('assets', "food2.png"))
font = pg.font.Font('freesansbold.ttf', 32)
food_rect = pg.Rect(-100,-100, 40, 40)
class Body:
    def __init__ (self,x,y,w,h,direction):
        self.rect = pg.Rect(x,y,w,h)
        self.direction = direction
        self.image = ""
    def set_image(self, image, anger=0):
        self.image = pg.transform.rotate(image,anger)
def move(player):
    for i in range(len(player)-1, 0, -1):
        player[i].rect.x = player[i-1].rect.x
        player[i].rect.y = player[i-1].rect.y
        player[i].direction = player[i-1].direction

    if player[0].direction == "right":
        player[0].rect.x += 40
    if player[0].direction == "left":
        player[0].rect.x += -40
    if player[0].direction == "up":
        player[0].rect.y += -40
    if player[0].direction == "down":
        player[0].rect.y += 40


def handle_control(player):
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and player[0].direction != "down":
        player[0].direction = "up"
    if keys[pg.K_s] and player[0].direction != "up":
        player[0].direction = "down"
    if keys[pg.K_a] and player[0].direction != "right":
        player[0].direction = "left"
    if keys[pg.K_d] and player[0].direction != "left":
        player[0].direction = "right"

def set_player_image(player):
    player[0].set_image(head_image,0)
    for i in range(1,len(player)):
        player[i].set_image(body_image)
def rotate_image(player):
    if player[0].direction == "right":
        player[0].set_image(head_image, 0)
    if player[0].direction == "left":
        player[0].set_image(head_image, 180)
    if player[0].direction == "up":
        player[0].set_image(head_image, 90)
    if player[0].direction == "down":
        player[0].set_image(head_image, -90)
    for i in range(1, len(player)):
        if player[i].direction == "right":
         player[i].set_image(body_image, 0)
        if player[i].direction == "left":
         player[i].set_image(body_image, 180)
        if player[i].direction == "up":
         player[i].set_image(body_image, 90)
        if player[i].direction == "down":
         player[i].set_image(body_image, -90)
def check_border(player):
    if player[0].rect.x >= 1280 and player[0].direction == "right":
        player[0].rect.x = 0
    if player[0].rect.x < 0 and player[0].direction == "left":
        player[0].rect.x = 1240
    if player[0].rect.y >= 720 and player[0].direction == "down":
        player[0].rect.y = 0
    if player[0].rect.y < 0 and player[0].direction == "up":
        player[0].rect.y = 680
def generate_food(food):
    x = random.randint(0,31)
    y = random.randint(0,17)
    food.x = 40*x
    food.y = 40*y
def eat_food(food, player, x,y,direction):
    if player[0].rect.colliderect(food):
        global point
        point += 1
        generate_food(food)
        player.append(Body(x,y,40,40,direction))
def check_end(player):
    for i in range(1,len(player)-1):
        if player[0].rect.colliderect(player[i].rect):
            return True
point = 0
running = True
status = "menu"
snake = [Body(40,0,40,40,"right"), Body(0,0,40,40,"right")]
while running:
  for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
  img = font.render("point: " + str(point),True,(0,0,0))
  if status == "menu":
    screen.fill("black")
    menu_text = font.render("Play", True, (255,255,255), "green")
    menu_textRect = menu_text.get_rect()
    menu_textRect.center = (WIDTH/2,HEIGHT/2)
    screen.blit(menu_text, menu_textRect)
    pg.display.update()
    if menu_textRect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]==True :
        status = "playing"
        generate_food(food_rect)
  if status == "gameover":
    screen.fill("white")
    quit_text = font.render("Quit", True, (0,0,0))
    again_text = font.render("Play Again", True, (0,0,0))
    quit_textRect = quit_text.get_rect()
    again_textRect = again_text.get_rect()
    pointRect = img.get_rect()
    pointRect.center = (WIDTH/2, HEIGHT/3)
    quit_textRect.center = (WIDTH/3*2,HEIGHT/3*2)
    again_textRect.center = (WIDTH/3,HEIGHT/3*2)
    screen.blit(img, pointRect)
    screen.blit(again_text, again_textRect)
    screen.blit(quit_text, quit_textRect)
    pg.display.update()
    if quit_textRect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]==True :
        running = False
    if again_textRect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]==True :
        status = "playing"
        point = 0
        snake = [Body(40,0,40,40,"right"), Body(0,0,40,40,"right")]
        generate_food(food_rect)


  if status == "playing":  
    rotate_image(snake)
    screen.blit(map_image,(0,0))
    screen.blit(img,(0,360))
    screen.blit(food_image, food_rect.topleft)
    handle_control(snake)
    last_x = snake[-1].rect.x
    last_y = snake[-1].rect.y
    last_direction = snake[-1].direction
    move(snake)
    check_border(snake)
    for i in range(len(snake)):
        screen.blit(snake[i].image, (snake[i].rect.x,snake[i].rect.y))
    print(snake[0].rect.topleft, snake[0].direction)
    eat_food(food_rect,snake,last_x,last_y,last_direction)
    if check_end(snake):
        status = "gameover"
    pg.display.update()
    clock.tick(10)
pg.quit()
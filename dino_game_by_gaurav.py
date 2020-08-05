import pygame
import math

# initialie program

pygame.init()

# set screen
screen = pygame.display.set_mode((400, 600))

# caption and  icon
pygame.display.set_caption("Dino By Gaurav")
icon = pygame.image.load("resourses\dinoo.png")
pygame.display.set_icon(icon)

# dino game object
dino_img = pygame.image.load("resourses\dino_one.png")
dinox = 50
dinoy = 485
dinoy_change = 0

# ground object
ground_img = pygame.image.load("resourses\dino land.png")
groundx = 0
groundy = 400
groundx_change = 0.9

# obstacle object
obstacle_img = pygame.image.load("resourses\obstcle.png")
obstaclex = 300
obstacley = 485
obstaclex_change = 0.8

#obstacle no 2

obstacle_img_second = pygame.image.load("resourses\obstacle.png")
obstacle_secondx = 500
obstacle_secondy= 495
obstacle_secondx_change = 0.8

#FLYING OBSTACLE

flying_object_img = pygame.image.load("resourses\object_flying.png")
flying_object_x = 1500
flying_object_y= 395
flying_object_x_change = 1.2


# game over  font
over_font = pygame.font.Font('freesansbold.ttf', 64)

# score font
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 42)
textX = 10
testY = 10


#--------------------GAME FUNTIONS----------------------

#PRINT SCORE
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

#PRINT GAME OVER
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (0, 250))

#PRINT OBSTACLE
def obstacle(x, y):
    screen.blit(obstacle_img, (x, y))

#PRINT SECOND OBSTACLE
def obstacle_second(x,y):
    screen.blit(obstacle_img_second, (x, y))

#print FLYIN OBJECT
def obstacle_flying_object(x,y):
    screen.blit(flying_object_img, (x, y))

#PRINT GROUND
def ground(x, y):
    screen.blit(ground_img, (x, y))

#PRINT DINO
def dino(x, y):
    screen.blit(dino_img, (x, y))

#COLLISION
def isCollision(obstaclex, obstacley, dinoX, dinoY):
    distance = math.sqrt(math.pow(obstaclex - dinoX, 2) + (math.pow(obstacley - dinoY, 2)))
    if distance < 30 or dinoy <=370 :
        return True
    else:
        return False
def isCollision_second_obstacle(obstacle_secondx,obstacle_secondy,dinoX,dinoY):
    distance = math.sqrt(math.pow(obstacle_secondx - dinoX, 2) + (math.pow(obstacle_secondy - dinoY, 2)))
    if distance < 30 or dinoy <=370 :
        return True
    else:
        return False
def isCollision_flying_object(flying_object_x,flying_object_y,dinoX,dinoY):
    distance = math.sqrt(math.pow(flying_object_x - dinoX, 2) + (math.pow(flying_object_y - dinoY, 2)))
    if distance < 30 or dinoy <=370 :
        return True
    else:
        return False



# LOOP VARIABLE
jumping = True

# MAIN GAME LOOP
while jumping:

    # BACKGROUND COLOUR
    screen.fill((255, 255, 255))

    # CLOSE GAME EVENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jumping = False

    # GROUND MOVEMENT
    groundx -= groundx_change
    if groundx <= -200:
        groundx = 0
        ground(groundx, groundy)

        # SCORE INCREASE BY ONE
        score_value = score_value + 10


    # ADD KEYBOARD KEYS TO MAKE DINO JUMP
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            dinoy_change = -0.8

    # DINO MOVEMENT
    dinoy = dinoy + dinoy_change
    if dinoy <= 395:
        dinoy_change = 0.8
        dinoy = dinoy + dinoy_change
    elif dinoy >= 485:
        dinoy_change = 0

    # OBSTACLE MOVEMENT
    obstaclex = obstaclex - obstaclex_change
    if obstaclex <= -5:
        obstaclex = 400

    #SECOND OBSTACLE MOVEMENT
    obstacle_secondx = obstacle_secondx - obstacle_secondx_change
    if obstacle_secondx <= -7:
        obstacle_secondx = 800

    #FLYING OBJECT MOVEMENT
    flying_object_x = flying_object_x - flying_object_x_change
    if flying_object_x <= -1:
        flying_object_x = 1233

    # OBSTACLE AND DINO COLLISION N GAME OVER
    collision = isCollision(obstaclex, obstacley, dinox, dinoy)
    Collision_second = isCollision_second_obstacle(obstacle_secondx,obstacle_secondy,dinox,dinoy)
    collision_of_flying_object = isCollision_flying_object(flying_object_x,flying_object_y,dinox,dinoy)
    if collision or Collision_second or collision_of_flying_object:
        dinoy_change = 0
        groundx_change = 0
        obstaclex_change = 0
        obstacle_secondx_change = 0
        flying_object_x_change = 0
        game_over_text()

    # SHOW SCORE ON TOP
    show_score(textX, testY)

    # DINO OBJECT PRINT
    dino(dinox, dinoy)

    # GROUND PRINT
    ground(groundx, groundy)

    # OBSTACLE PRINT
    obstacle(obstaclex, obstacley)
    obstacle_second(obstacle_secondx, obstacle_secondy)
    obstacle_flying_object(flying_object_x,flying_object_y)


    # UPDATE THE SCREEN
    pygame.display.update()

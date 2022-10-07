import pygame
from pygame.locals import *
import math
import random
from pygame import mixer
import button

# initializes pygame
pygame.mixer.pre_init()
mixer.init()
pygame.init()

# Create screen - this is what display when games runs
WIDTH, HEIGHT = 800, 500 
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Kingdom Transformation (Hangman!)")


# frames per second
FPS = 60
clock = pygame.time.Clock()


#--------
# CONSTANTS
#--------

# variables for letter button
RADIUS = 20
GAP = 15
letters = [] 
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65


# variables for game
# game_paused = False
# menu_state = "main"
game_status = 0
words = ["USAGI", "SAILOR MOON", "SAILOR MARS", "SAILOR MINI MOON", "SAILOR JUPITER", "SAILOR VENUS", "SAILOR SATURN", "MOON TIARA MAGIC", "SPACE SWORD BLASTER", "CRESCENT BEAM",
 "MERCURY AQUA RHAPSODY", "WORLD SHAKING", "FIRE SOUL", "SUPREME THUNDER", "TUXEDO MASK", "LUNA", "ARTEMIS", "DIANA", "SAILOR STARLIGHTS", "SERENA", "RINI", "HOLY GRAIL" ]
word = random.choice(words)
guesses = [" "]
start_game = False


#--------
# CONSTANTS
#--------



# Background music
mixer.music.load("assets/smtheme.ogg")
mixer.music.set_volume(0.25)
mixer.music.play(-1)

# load sounds
sm_fx = pygame.mixer.Sound("assets/jingle.ogg")
sm_fx.set_volume(0.35)

# load images
# button imgs
start_img = pygame.image.load("assets/start.png")
exit_img = pygame.image.load("assets/exit.png")
restart_img = pygame.image.load("assets/restart.png")
start_screen = pygame.image.load("assets/smb.png")
start_screen = pygame.transform.scale(start_screen, (WIDTH, HEIGHT))
sm_gf = pygame.image.load("assets/crying.gif")
sm2_gf = pygame.image.load("assets/sailormoon.jpeg")

#store transformation images in a list
images = []
for i in range(13):
    image = pygame.image.load("assets/hangman" + str(i) + ".png")
    images.append(image)


# colors variable
WHITE = (255, 255, 255)
PINK = (134, 46, 156)


# Letters front 
font = pygame.font.SysFont('comicsans', 20)
TITLE = pygame.font.SysFont('comicsans', 30)


# to achieve two rows by using i % 13. i // 13 allows for whole numbers division with no remainders
game_status = 0
for i in range(26):
    x = startx +  GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


def draw():
    win.fill(WHITE)

# Title 
    text = TITLE.render("Moon Kingdom Transformation Hangman", 1, PINK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

# draw word that will store guesses of word
    display_guesses = ""
    for letter in word:
        if letter in guesses:
            display_guesses += letter + " "
        else:
            display_guesses += "_ "
    text = TITLE.render(display_guesses, 1, PINK)
    win.blit(text, (200, 300))


# draw buttons with letters A-Z
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, PINK, (x, y), RADIUS, 3)
            text = font.render(ltr, 1, PINK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
            #letter_Sound = mixer.Sound("Sailor-Moon-Jingle.ogg")
            #letter_Sound.play()

# draw image with x and y position we want images display
    win.blit(images[game_status], (270, 80))
    pygame.display.update()
    


def won_lost_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    
    text = font.render(message, 1, PINK)
    win.blit(text, (WIDTH/2 - text.get_width()/2,  HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    #pygame.time.delay(3000)




start_button = button.Button(WIDTH // 2 - 400, HEIGHT // 2 - 80, start_img, 1)
exit_button = button.Button(WIDTH // 2 - -180, HEIGHT // 2 + -80, exit_img, 1)
restart_button = button.Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, restart_img, 2)


# Main Loop while loop run is equal to true keep running this
# loop if game is lost the loop exits 
run = True
while run:

# Clock object to ensure game keep track of time
    clock.tick(FPS)

    if start_game == False:
        #main menu
        
        win.blit(start_screen,(0,0))
        
        

        if start_button.draw(win):
                start_game = True
        if exit_button.draw(win):
                run = False
    else:           
        draw()
            
   
          

# event triggers stored in the for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# position of mouse in the x and y of mouse in the window           
        if event.type == pygame.MOUSEBUTTONDOWN:
# Check for collision for the buttons
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)  ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
# True value is equal to letter true by changing it to false the button disappear
                        letter[3] = False
                        guesses.append(ltr)
                        sm_fx.play()
                        if ltr not in word:
                            game_status += 1
  
# reset

   

# for loop to see if game is won
    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break
    if won:
        
        won_lost_message("Winner: Moon Prism Power Make UP!")
        win.blit(sm2_gf,(30,60))
        pygame.display.update()
        pygame.time.delay(8000)
     
        
        
# to see if game is loss
    if game_status == 13:
        won_lost_message("Game Over: Usagi is a crybaby")
        win.blit(sm_gf, (300, 60))
        pygame.display.update()
        pygame.time.delay(8000)
        break


                       
    pygame.display.update() 
pygame.quit()




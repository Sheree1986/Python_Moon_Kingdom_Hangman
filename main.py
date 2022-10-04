import pygame
import math
import random


pygame.init()
# What display when games runs
WIDTH, HEIGHT = 800, 500 
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moon Kingdom Transformation (Hangman!)")

# load images
images = []
for i in range(13):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# variables for letter button


RADIUS = 20
GAP = 15
letters = [] 
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

# to achieve two rows by using i % 13. i // 13 allows for whole numbers division with no remainders
for i in range(26):
    x = startx +  GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Letters front 
font = pygame.font.SysFont('comicsans', 30)
TITLE = pygame.font.SysFont('comicsans', 40)

# variables for game
game_status = 0
words = ["USAGI", "SAILOR MOON", "SAILOR MARS", "SAILOR MINI MOON", "SAILOR JUPITER", "SAILOR VENUS", "SAILOR SATURN", "MOON TIARA MAGIC", "SPACE SWORD BLASTER", "CRESCENT BEAM", "MERCURY AQUA RHAPSODY", "WORLD SHAKING", "FIRE SOUL", "SUPREME THUNDER" ]
word = random.choice(words)
guesses = [" "]

# colors variable
WHITE = (255, 255, 255)
PINK = (134, 46, 156)

#GIF = pygame.image.load("hangmantransformation.gif")

# frames per second
FPS = 60
clock = pygame.time.Clock()
run = True

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
    text = font.render(display_guesses, 1, PINK)
    win.blit(text, (400, 200))



# draw buttons with letters A-Z
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, PINK, (x, y), RADIUS, 3)
            text = font.render(ltr, 1, PINK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

# draw image with x and y position we want images display
    win.blit(images[game_status], (30, 100))
    pygame.display.update()


def won_lost_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = font.render(message, 1, PINK)
    win.blit(text, (WIDTH/2 - text.get_width()/2,  HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
        



# while loop run is equal to true keep running this
# loop if game is lost the loop exits
while run:

# Clock object to ensure game keep track of time
    clock.tick(FPS)

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
                        if ltr not in word:
                            game_status += 1
    draw()
# for loop to see if game is won
    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break

    if won:
        won_lost_message("Moon Prism Power Make UP!")

        break

# to see if game is loss

    if game_status == 12:
        won_lost_message("Usagi is a crybaby")
        break
                       #testing push to main 

pygame.quit()



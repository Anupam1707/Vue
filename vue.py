import pygame
import sys
from time import strftime
import random
import requests
from fetchify import fetch
from io import BytesIO

# Get a list of file names for all images in the folder
# background_images = [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

background_images = [file['name'] for file in requests.get("https://api.github.com/repos/Anupam1707/Vue/contents").json() if file['type'] == 'file']
background_images.remove("vue.py")
background_images.remove("README.md")
# background_images.remove("LICENCE")

def time():
    stringt = strftime('%H:%M %p')
    stringd = strftime('%d/%m/%Y')
    formatted_date = strftime('%d %b %Y')
    labelt= fontt.render(stringt, True, (255, 255, 255))
    labeld= fontd.render(formatted_date, True, (255, 255, 255))
    # Set the label to the left bottom (10 pixels from the left, 10 pixels from the bottom)
    screen.blit(labelt, (50, screen_height - labelt.get_height() - 100))
    screen.blit(labeld, (50, screen_height - labeld.get_height() - 40))

def change_background():
    # Load the next background image
    next_image = pygame.image.load(BytesIO(fetch(random.choice(background_images), "vue", image=True)))
    next_image = pygame.transform.scale(next_image, (width + 100, height + 100))

    # Fade effect
    alpha = 0
    step = 10
    while alpha <= 255:
        next_image.set_alpha(alpha)
        screen.blit(next_image, (0, 0))
        time()  # Update the time label
        pygame.display.flip()
        pygame.time.delay(20)
        alpha += step

    # Schedule the function to run again after a delay
    pygame.time.set_timer(pygame.USEREVENT, background_change_interval)

# Initialize Pygame
pygame.init()

# Set up the window

pygame.display.set_caption("Show Mode Time Display")
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
width, height = screen_width, screen_height

# List of background images

# Set up the font for displaying time
fontt = pygame.font.Font(None, 175)
fontd = pygame.font.Font(None, 100)

# Set up a timer event for changing the background
background_change_interval = 7000  # Change every 5 seconds (in milliseconds)
pygame.time.set_timer(pygame.USEREVENT, background_change_interval)

# Run the main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            change_background()

    pygame.time.delay(100)

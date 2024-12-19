'''
Moram da ucitam pdf
Da izdvojim u 2 txt fajla, pitanja i njihove odgovore
Mora da se napravi UI koji se na klik da izabere random pitanje
Treba da mi ga prikaze ili u terminalu ili da mi izbaci pitanje
Treba da mogu klikom da pogledam resenje ili da idem
    na sledecu karticu
'''
import pandas as pd
import keyboard as kb
import time
import random
import pygame 
import sys

counter = 0
q_count = 1
file = open("text.txt", 'r')
resenja = open("resenja.txt", 'r+')
pitanja = open('pitanja.txt', 'r+')
q_dict = {}
a_dict = {}
file_lines = file.readlines()

#spliting data int questions and answers
for line in file_lines:
    if(counter == 0):
        counter+=1
        key, value = q_count, line
        q_dict[key] = value
    else: 
        counter = 0
        key, value = q_count, line
        a_dict[key] = value
        q_count+=1

with open('resenja.txt', 'w') as f:
    for key,value in a_dict.items():
        f.write(f"{key}:{value}\n")
        
with open('pitanja.txt', 'w') as f:
    for key,value in q_dict.items():
        f.write(f"{key}:{value}\n")

#u sustini je kao igrica
#izbaci mi karticu i ja klikom predjem na drugu
#pogledam odgovor ili zavrsim igru
pygame.init()
width, height = 500, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flash kartice")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
screen.fill(WHITE)
font = pygame.font.SysFont('Ariel', 36)

#Creating buttons
button_width, button_height = 150, 50
button_margin = 20  # Space between buttons
button_y = height - button_height - 10
button1_rect = pygame.Rect(width // 4 - button_width // 2, button_y, button_width, button_height)
button2_rect = pygame.Rect(3 * width // 4 - button_width // 2, button_y, button_width, button_height)

#drawing the button
def draw_button(rect, text):
    pygame.draw.rect(screen, BLUE, rect)  # Draw button (blue)
    # Render the text and center it inside the button
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

#Writing out the question
def write_q(reci):
    text = font.render(reci, True, BLACK)
    text_rect = text.get_rect(center=(width//2, height//3))
    screen.blit(text, text_rect)

#run time lol
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            # Check if mouse is inside the button1 rectangle
            if button1_rect.collidepoint(mouse_pos):
                print("Sledece pitanje!")
                # random_broj = random.randint(1, q_count)
                # reci = q_dict[random_broj]
            # Check if mouse is inside the button2 rectangle
            if button2_rect.collidepoint(mouse_pos):
                print("Odgovor na pitanje!")

    # Fill the screen with white background
    screen.fill(WHITE)

    # Draw the buttons
    draw_button(button1_rect, 'Next')
    draw_button(button2_rect, 'Answer')
    random_broj = random.randint(1, q_count)
    
    write_q("pitanje")

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()

#generating a image to put a question onto



i = 1
while i<=q_count:
    random_broj = random.randint(1, q_count)
    ulaz = input()
    if ulaz =="n":
        print(q_dict[random_broj])
        i+=1
    elif ulaz == "a":
        print(a_dict[random_broj])
    else: 
        print("Kraj\n")
        break
file.close()
resenja.close()
pitanja.close()

        




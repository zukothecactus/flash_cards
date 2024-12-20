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

file.close()
resenja.close()
pitanja.close()

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
    pygame.draw.rect(screen, (80,200,120), rect)  # Draw button (blue)
    # Render the text and center it inside the button
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

#Writing out the question
def write_q(reci):
    fontic = pygame.font.SysFont('Times New Roman', 50)
    text = fontic.render(reci, True, BLACK)
    text_rect = text.get_rect(center=(width//2, height//3))
    screen.blit(text, text_rect)

random_text = 'Pitanja'
answer_key = -1
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            
            if button1_rect.collidepoint(mouse_pos):
                print("Sledece pitanje!")
                random_key = random.choice(list(q_dict.keys()))
                answer_key = random_key
                random_text = q_dict[random_key]
                
            if button2_rect.collidepoint(mouse_pos):
                if(answer_key != -1):
                    print("Odgovor na pitanje!")
                    random_text = a_dict[answer_key]
                else:
                    print("Morate ucitati neko pitanje")

    # Fill the screen with white background
    screen.fill((255, 229, 180))

    # Draw the buttons
    draw_button(button1_rect, 'Next')
    draw_button(button2_rect, 'Answer')
    random_broj = random.randint(1, q_count)
    
    write_q(random_text.strip())

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()

#generating a image to put a question onto


        




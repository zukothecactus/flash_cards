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
counter = 0

q_count = 1

file = open("text.txt", 'r')
resenja = open("resenja.txt", 'r+')
pitanja = open('pitanja.txt', 'r+')

file_lines = file.readlines()

for line in file_lines:
    if(counter == 0):
        counter+=1
        line = str(q_count)+'.'+line
        pitanja.write(line)
    else: 
        counter = 0
        line = str(q_count)+'.'+line
        resenja.write(line)
        q_count+=1

print("Press 'n' for the next question\nPress 'q' to quit")
while True:
    if kb.is_pressed('n'):
        print("Sledece pitanje")
        a = input()
    if kb.is_pressed('q'):
        print("Kraj")
        break
    
        
        
file.close()
resenja.close()
pitanja.close()

        




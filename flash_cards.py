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

counter = 0

q_count = 1

file = open("text.txt", 'r')
resenja = open("resenja.txt", 'r+')
pitanja = open('pitanja.txt', 'r+')
q_dict = {}
a_dict = {}
file_lines = file.readlines()

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


print("Press 'n' for the next question\nPress 'q' to quit\nPress 'a' to get the answer\n")

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
'''
while True:
    if kb.is_pressed('n'):
        random_broj = random.randint(1, q_count)
        print("Sledece pitanje je:\n")
        print(q_dict[random_broj])
        time.sleep(10)
        if kb.is_pressed('a'):
            print("Odgovor je: "+ a_dict[random_broj])
    if kb.is_pressed('q'):
        print("Kraj")
        break
    
'''
        
file.close()
resenja.close()
pitanja.close()

        




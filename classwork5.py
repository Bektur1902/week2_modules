import os
import random

print('Текущяя директория: ', os.getcwd())
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

count = 0
while count < 5:
    if not os.path.isdir('folder'):
        os.mkdir('folder')
        f = open("random(names).txt")
        f.close()



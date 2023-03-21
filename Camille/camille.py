import psutil
import itertools
import os

letters = 'abcdefghijklmnopqrstuvwxyz'
x = 0
dossier = "cache/"
dossier1 = "cache"
if not os.path.exists(dossier1):
    os.mkdir(dossier1)

disk = psutil.disk_usage('/')
total = disk.total / (1024*1024*1024)
Utilisé = disk.used / (1024*1024*1024)
Disponible = disk.free / (1024*1024*1024)

taille = int((disk.free / (1024*1024*1024))/0.010)
combinations = itertools.combinations(letters, 10)

for combination in combinations:
    x += 1
    txt = dossier + ''.join(combination) + ".txt"
    fichier = open(txt, "w+", encoding="utf-8")
    fichier.write("z"*10240000)
    if x > taille:
        break
fichier.close()
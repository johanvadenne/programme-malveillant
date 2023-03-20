import psutil
import itertools

letters = 'abcdefghijklmnopqrstuvwxyz'
x = 0

disk = psutil.disk_usage('/')
print(f"Total: {disk.total / (1024*1024*1024):.2f} GB")
print(f"Utilisé: {disk.used / (1024*1024*1024):.2f} GB")
print(f"Disponible: {disk.free / (1024*1024*1024):.2f} GB")


combinations = itertools.combinations(letters, 10)

for combination in combinations:
    x += 1
    txt = ''.join(combination)
    fichier = open(txt, "w+", encoding="utf-8")
    fichier.write("z"*1000000000)
    print(txt)
    if x > 1:
        break

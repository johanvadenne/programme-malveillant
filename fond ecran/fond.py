import ctypes

# chemin complet vers le fichier image que vous souhaitez utiliser comme fond d'écran
image_path = r"Y:\PARTAGE\SQL-serveur\vadenne johan\blague\fonddecran\1.jpg"

# définit le fond d'écran
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
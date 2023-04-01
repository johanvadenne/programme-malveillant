import ctypes
import win32gui

# chemin complet vers le fichier image que vous souhaitez utiliser comme fond d'écran
image_pathp = r"D:\Johan\GitHub\virus\fond ecran\ecranp.jpg"
image_pathv = r"D:\Johan\GitHub\virus\fond ecran\ecranv.jpg"

# définit le fond d'écran
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_pathp, 0)


# Trouver la fenêtre de l'écran de verrouillage
hwnd = win32gui.FindWindow("LockAppHost", None)

# Modifier le texte affiché sur l'écran de verrouillage
win32gui.SendMessage(hwnd, 0x0111, 0x0100, "Nouveau texte d'écran de verrouillage")

# Modifier l'image affichée sur l'écran de verrouillage
win32gui.SystemParametersInfo(0x0014, 0, image_pathv , 0)
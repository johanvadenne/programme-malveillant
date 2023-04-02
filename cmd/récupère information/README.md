# Français

## le fichier info.bat bat va récupérer toute les information sur votre machine

> ### ipconfig /all >> ipconfig.txt
>
>permet d'avoir toutes les caractéristiques des connexions réseaux : adresse IP, adresse MAC… ipconfig /release : libère les connexions. ipconfig /renew : rétablit les connexions. ipconfig /flushdns : vide le cache de la résolution DNS.

> ### systeminfo >> systeminfo.txt
>
> permet de générer un résumé de la configuration matérielle et logicielle d'un ordinateur.


> ### for /f "skip=9 tokens=1,2 delims=:" %%i in ('netsh wlan show profiles') do @if "%%j" NEQ "" (echo SSID: %%j & netsh wlan show profile %%j key=clear) >> infowifi.txt
>
> permet de récupérer toutes les informations sur les appareils wii que vous vous êtes déjà (nom, mot de passe, type de cryptage, etc...).

>curl checkip.amazonaws.com >> ip.txt
>
> permet de récupé votre adresse ip public.

> commande >> nom_ficher.txt
>
> permet d'enregistrer les informations dans un fichier txt

# English

## the info.bat file will retrieve all the information about your machine

> ipconfig /all >> ipconfig.txt
>
>ipconfig /release : release connections. ipconfig /renew : restore connections. ipconfig /flushdns : empty the DNS resolution cache.

> ### systeminfo >> systeminfo.txt
>
> generates a summary of the hardware and software configuration of a computer.


> ### for /f "skip=9 tokens=1,2 delims=:" %%i in ('netsh wlan show profiles') do @if "%%j" NEQ "" (echo SSID: %%j & netsh wlan show profile %%j key=clear) >> infowifi.txt
>
> allows you to retrieve all the information about the wii devices you already have (name, password, encryption type, etc...).

>curl checkip.amazonaws.com >> ip.txt
>
> allows to recover your public IP address.

> command >> file_name.txt
>
> allows to save the information in a txt file